import pandas as pd
import numpy as np
import warnings
import os
import datetime
import plotly.graph_objects as go
from typing import Optional, Literal, Union
from collections.abc import Iterable, Mapping


DatetimeType = Union[float, str, datetime.date, datetime.datetime]


def _load_table(
        filename: str | os.PathLike, required_cols: Iterable,
        optional_cols: Optional[list] = None, index_col: Optional[str] = None,
        dtype: Optional[Mapping] = None
    ) -> pd.DataFrame:
    """
    Confirm that the given GTFS table contains all required columns
    and load into a DataFrame if it does. Otherwise, raise a ValueError.

    :param filename: path to file to read
    :param required_cols: columns that must be included in the table
        If they are missing, raise a ValueError.
    :param optional_cols: columns that should be included in the
        returned DataFrame if they are present. No error will be
        raised if they are missing.
    :param dtype: dict giving column data types, optional
    :return: DataFrame of loaded data, or raise an appropriate error
    """
    df = pd.read_csv(filename, index_col=index_col, dtype=dtype)
    if all(c in df.columns for c in required_cols):
        if optional_cols is not None:
            if not isinstance(optional_cols, list):
                raise TypeError(
                    'Expected type list, but received type {}'.format(
                        type(optional_cols)
                    )
                )

            present_optional_cols = [
                c for c in optional_cols if c in df.columns]

            return df[required_cols + present_optional_cols]

        else:
            return df[required_cols]

    else:
        missing_cols = [c for c in required_cols if c not in df.columns]
        raise ValueError(
            'Columns {} not present in {}'.format(
                missing_cols, filename
            )
        )


def _haversine_np(
        lon1: np.ndarray, lat1: np.ndarray,
        lon2: np.ndarray, lat2: np.ndarray
    ) -> np.ndarray:
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.

    Adapted from https://stackoverflow.com/a/29546836/8576714
    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(
        dlon / 2.0) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6378.137 * c
    miles = km / 1.609
    return miles


def _manhattan_np(
        lon1: np.ndarray, lat1: np.ndarray,
        lon2: np.ndarray, lat2: np.ndarray
    ) -> np.ndarray:
    """
    Calculate the Manhattan (l1-norm) distance between two points
    on the earth (specified in decimal degrees)

    Works by calculating 2 haversine distances.
    """
    return _haversine_np(lon1, lat1, lon2, lat1) + _haversine_np(
        lon2, lat1, lon2, lat2
    )


def add_deadhead(trips_df: pd.DataFrame):
    """
    Add estimated deadhead to DataFrame of trips
    """
    trips_df = trips_df.sort_values(by=['block_id', 'trip_idx'])
    block_gb = trips_df.groupby('block_id')
    dh_dfs = list()
    for _, block_df in block_gb:
        block_df[['dh_dest_lat', 'dh_dest_lon']] = block_df[
            ['start_lat', 'start_lon']].shift(-1)
        dh_dfs.append(block_df)
    trips_df = pd.concat(dh_dfs)

    # Gather unique OD pairs for all deadhead trips
    od_pairs = trips_df[
        ['end_lat', 'end_lon', 'dh_dest_lat', 'dh_dest_lon']
    ]
    od_pairs = od_pairs.drop_duplicates().dropna().reset_index(drop=True)

    # Use Manhattan distance to calculate deadhead distance. Much
    # faster/easier than using a distance API and should be close.
    od_pairs['dh_dist'] = _manhattan_np(
        od_pairs['end_lon'], od_pairs['end_lat'],
        od_pairs['dh_dest_lon'], od_pairs['dh_dest_lat']
    )

    # Merge DH dists into trip DF
    merged_trips = pd.merge(
        trips_df, od_pairs,
        on=['end_lat', 'end_lon', 'dh_dest_lat', 'dh_dest_lon'],
        how='left'
    ).fillna({'dh_dist': 0})

    return merged_trips.drop(
        columns=['dh_dest_lat', 'dh_dest_lon']
    )


def get_shape(shapes_df: pd.DataFrame, shape_id: str) -> tuple:
    """
    Get the shape of a trip (as a sequence of coordinates)
    :param shapes_df: DF of all trip shapes, from GTFS shapes.txt
    :param shape_id: shape ID requested
    :return: 2-tuple of pd.Series giving all longitudes (0) and
        latitudes (1) of points in shape
    """
    this_shape = shapes_df[shapes_df['shape_id'] == shape_id]
    this_shape.sort_values(by='shape_pt_sequence')
    return this_shape['shape_pt_lon'], this_shape['shape_pt_lat']


def calculate_shape_dists(
        shapes_df: pd.DataFrame, shape_ids: Iterable
    ) -> pd.DataFrame:
    """
    Use the shape points provided in shape_df to calculate the
    total length of all shapes included in the table.
    """
    shapes_df = shapes_df[shapes_df['shape_id'].isin(shape_ids)]
    gb = shapes_df.groupby('shape_id')
    shapes_list = list()
    dists_list = list()
    for shape_id, shape_grp in gb:
        shape_grp = shape_grp.sort_values(
            by='shape_pt_sequence').reset_index()
        # Add columns that give coordinates of last point
        shape_grp[['prev_lat', 'prev_lon']] = shape_grp[
            ['shape_pt_lat', 'shape_pt_lon']].shift(1)
        # First point in the shape doesn't have a predecessor. Just
        # set it to itself so the distance is zero.
        shape_grp.loc[0, 'prev_lat'] = shape_grp.loc[0, 'shape_pt_lat']
        shape_grp.loc[0, 'prev_lon'] = shape_grp.loc[0, 'shape_pt_lon']
        # Calculate distance between points
        shape_grp['seq_dist'] = _haversine_np(
            shape_grp['shape_pt_lon'], shape_grp['shape_pt_lat'],
            shape_grp['prev_lon'], shape_grp['prev_lat'])
        # Add total distance to list
        shapes_list.append(shape_id)
        dists_list.append(shape_grp['seq_dist'].sum())

    # Build dataframe of results
    manual_dists = pd.DataFrame(
        {'shape_id': shapes_list, 'manual_dist': dists_list}
    ).set_index('shape_id')
    return manual_dists


def plot_trips_and_terminals(trips_df: pd.DataFrame, shapes_df: pd.DataFrame):
    """
    Plot all trips in the given DataFrame based on their shape traces
    and terminal coordinates.
    """
    # Compile terminal counts
    start_cts = trips_df.groupby(
        ['start_lat', 'start_lon']).count()['route_id'].rename('start')
    start_cts.index.set_names(['lat', 'lon'], inplace=True)
    end_cts = trips_df.groupby(
        ['end_lat', 'end_lon']).count()['route_id'].rename('end')
    end_cts.index.set_names(['lat', 'lon'], inplace=True)
    all_cts = pd.merge(
        start_cts, end_cts, left_index=True, right_index=True, how='outer')
    all_cts = all_cts.fillna(0)
    all_cts['total'] = all_cts['start'] + all_cts['end']
    all_cts = all_cts.sort_values(by='total', ascending=False).reset_index()
    all_cts['name'] = ''
    all_cts['symbol'] = 'circle'
    all_cts['size'] = all_cts['total']
    all_cts['label_name'] = [
        '{} trips start here, {} trips end here'.format(
            int(all_cts['start'][i]), int(all_cts['end'][i]))
        for i in range(len(all_cts))]
    all_cts['color'] = 'blue'

    # Trip terminals
    # Marker size: scale linearly from minimum to maximum
    min_marker = 10
    max_marker = 20
    msize = np.round(min_marker + (max_marker - min_marker) * (
            all_cts['size'] - all_cts['size'].min())/all_cts['size'].max())
    
    fig = go.Figure()
    new_trace = go.Scattermap(lat=all_cts['lat'], lon=all_cts['lon'],
                                 showlegend=True, hoverinfo='text',
                                 mode='markers', text=all_cts['label_name'],
                                 marker=go.scattermap.Marker(
                                     color='rgba(60, 120, 255, 1)',
                                     size=msize),
                                 name='Trip Start/End Locations    ')
    fig.add_trace(new_trace)

    # Trips
    shape_cts = trips_df.groupby('shape_id').count()['route_id'].sort_values()
    for shp in shape_cts.index:
        shape_pts = get_shape(shapes_df, shp)
        shape_pt_df = pd.DataFrame(shape_pts).transpose()
        alpha = 0.2 + 0.5 * shape_cts[shp] / max(shape_cts)
        rgba_str = 'rgba(255, 80, 80, {:.2f})'.format(alpha)

        new_trace = go.Scattermap(
            mode='lines',
            lat=shape_pt_df["shape_pt_lat"],
            lon=shape_pt_df["shape_pt_lon"],
            showlegend=False, hoverinfo='skip',
            line={'color': rgba_str, 'width': 2})
        fig.add_trace(new_trace)

    # Trace for legend
    new_trace = go.Scattermap(
        mode='lines', lat=shape_pt_df["shape_pt_lat"],
        lon=shape_pt_df["shape_pt_lat"], showlegend=True,
        line={'color': 'rgba(255, 80, 80, 0.9)'},
        name='Passenger Trip   ')
    fig.add_trace(new_trace)

    # Reverse order to put markers on top
    fdata = fig.data
    fig.data = tuple(list(fdata[1:]) + [fdata[0]])
    fig.update_layout(
        legend=dict(
            orientation="h", yanchor="bottom", y=1.01,
            xanchor="right", x=0.98, font={'size': 14},
        ),
        margin=dict(l=0, r=0, t=5, b=0))
    # Set default map bounds
    fig.update_layout(
        map = {
            'bounds': {
                'north': all_cts.lat.max() + 1,
                'south': all_cts.lat.min() - 1,
                'east': all_cts.lon.max() + 1,
                'west': all_cts.lon.min() - 1
            }
        }
    )

    return fig


def filter_blocks_by_route(
        trips: pd.DataFrame, routes: Iterable,
        route_column: Literal['route_short_name', 'route_id'] = 'route_short_name',
        route_method: Literal['exclusive', 'inclusive'] = 'exclusive'
    ) -> pd.DataFrame:
    gb = trips.groupby('block_id')
    route_blocks = list()
    for block_id, subdf in gb:
        if route_method == 'exclusive':
            include_block = all(subdf[route_column].isin(routes))

        elif route_method == 'inclusive':
            include_block = any(subdf[route_column].isin(routes))

        else:
            raise ValueError(
                'route_method must be either "exclusive" or "inclusive"'
            )

        if include_block:
            route_blocks.append(block_id)

    return trips[trips['block_id'].isin(route_blocks)]


def get_all_trip_data(
        gtfs_path: str | os.PathLike,
        date: DatetimeType,
        routes: Optional[Iterable[str]] = None,
        route_method: Optional[Literal['exclusive', 'inclusive']] = None,
    ) -> pd.DataFrame:
    """
    Wrapper function to get all gtfsblocks data for trips completed by
    the specfied routes on a specific date.
    """
    # Read in complete feed
    gtfs = Feed.from_dir(gtfs_path)
    # Filter down to trips on the input date
    day_trips = gtfs.get_trips_from_date(date)
    if routes is not None:
        # Filter down to trips on the given routes
        day_trips = filter_blocks_by_route(
            trips=day_trips, routes=routes, route_method=route_method
        )

    return add_deadhead(gtfs.add_trip_data(day_trips, date))


class Feed:
    """
    Feed class for reading and processing GTFS data. This class handles
    reading in static GTFS feeds and parsing them for relevant block-
    level features including trip distances, start and end points,
    start and end times, and more.

    The typical use case is to read in data with the alternate
    constructor Feed.from_dir(), specifying a directory where the
    necessary files are stored.
    """
    def __init__(
            self, calendar_file: str | os.PathLike,
            calendar_dates_file: str | os.PathLike,
            trips_file: str | os.PathLike,
            shapes_file: str | os.PathLike,
            routes_file: str | os.PathLike,
            stop_times_file: str | os.PathLike,
            columns: Optional[Mapping] = None
        ):
        """
        Constructor for Feed class.

        :param calendar_file:
        :param calendar_dates_file:
        :param trips_file:
        :param shapes_file:
        :param routes_file:
        :param stop_times_file:
        """
        # TODO: also require agency file and build in filtering by
        # agency.
        REQUIRED_COLS = {
            'trips': [
                'trip_id', 'route_id', 'service_id', 'block_id', 'shape_id'
            ],
            'routes': ['route_id', 'route_short_name', 'route_type'],
            'calendar': [
                'service_id', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday', 'start_date',
                'end_date'
            ],
            'calendar_dates': ['service_id', 'date', 'exception_type'],
            'shapes': [
                'shape_id', 'shape_pt_lat', 'shape_pt_lon', 'shape_pt_sequence'
            ],
            'stop_times': ['trip_id', 'stop_sequence', 'arrival_time']
        }

        # Add user-supplied columns as desired. Treat them as required
        # so that they get an error if the column is not present.
        combined_cols = REQUIRED_COLS.copy()
        if columns is not None:
            for file_type in columns:
                if file_type not in REQUIRED_COLS:
                    raise ValueError(
                        '{} is not a valid file type for column '
                        'specification. Options are: {}'.format(
                            file_type, list(REQUIRED_COLS.keys())
                        )
                    )
                
                # Add user-requested columns
                combined_cols[file_type] = list(
                    set(
                        REQUIRED_COLS[file_type] + columns[file_type]
                    )
                )

        # Load each
        self.trips = _load_table(
            filename=trips_file,
            required_cols=combined_cols['trips'],
            dtype={
                'trip_id': str,
                'route_id': str,
                'service_id': str,
                'block_id': str,
                'shape_id': str
            }
        )
        self.routes = _load_table(
            filename=routes_file,
            required_cols=combined_cols['routes'],
            optional_cols=['route_desc'],
            dtype={
                'route_id': str,
                'route_short_name': str,
                'route_type': int
            }
        )
        self.routes.set_index('route_id', inplace=True)
        # Only retain bus routes
        self._filter_by_trip_type()

        # At least one of calendar.txt and calendar_dates.txt is
        # required, but it's okay to have just one of them.
        try:
            self.calendar = _load_table(
                filename=calendar_file,
                required_cols=combined_cols['calendar'],
                dtype={
                    'service_id': str
                }
            )
            self.calendar['start_date'] = pd.to_datetime(
                self.calendar['start_date'].astype(str))
            self.calendar['end_date'] = pd.to_datetime(
                self.calendar['end_date'].astype(str))
        except FileNotFoundError:
            self.calendar = None

        try:
            self.calendar_dates = _load_table(
                filename=calendar_dates_file,
                required_cols=combined_cols['calendar_dates'],
                dtype={
                    'service_id': str
                }
            )
            self.calendar_dates['date'] = pd.to_datetime(
                self.calendar_dates['date'].astype(str))
        except FileNotFoundError:
            self.calendar_dates = None

        if self.calendar is None and self.calendar_dates is None:
            raise ValueError(
                'At least one of calendar.txt and calendar_dates.txt must '
                'be provided.'
            )

        self.shapes = _load_table(
            shapes_file,
            required_cols=combined_cols['shapes'],
            dtype={
                'shape_id': str
            }
        )
        self.stop_times = _load_table(
            stop_times_file,
            required_cols=combined_cols['stop_times'],
            dtype={'trip_id': str}
        )
        self.shapes_summary = None

    @classmethod
    def from_dir(
            cls,
            dir_name: str | os.PathLike,
            columns: Optional[Mapping] = None
        ):
        """
        Construct a Feed object from the path to a directory where
        static GTFS files are stored.
        """
        trips_file = '{}/trips.txt'.format(dir_name)
        calendar_file = '{}/calendar.txt'.format(dir_name)
        calendar_dates_file = '{}/calendar_dates.txt'.format(dir_name)
        shapes_file = '{}/shapes.txt'.format(dir_name)
        routes_file = '{}/routes.txt'.format(dir_name)
        stop_times_file = '{}/stop_times.txt'.format(dir_name)

        return cls(
            calendar_file=calendar_file,
            calendar_dates_file=calendar_dates_file,
            trips_file=trips_file,
            shapes_file=shapes_file,
            routes_file=routes_file,
            stop_times_file=stop_times_file,
            columns=columns
        )

    def _filter_by_trip_type(self):
        """
        Remove any non-bus trips from the data.
        """
        # Which routes are not bus routes?
        bad_rts = self.routes[
            self.routes['route_type'] != 3].index.tolist()
        # Exclude any trips on those routes.
        self.trips = self.trips[
            ~self.trips['route_id'].isin(bad_rts)]

    def summarize_shapes(self, shape_ids: list):
        """
        Create a summary table of key shape details.

        This method aggregates the data in shape_df to get some details
        needed by our models: the lat/lon coordinates of the start and
        end location of the trip and its total distance. This is stored
        as self.shapes_summary so we can efficiently access this
        summary info when needed.

        :param shape_ids: list of shape_id values that should be
            summarized. saves computation time if we don't need to
            process all shape_ids in the table.
        """
        if self.shapes_summary is None:
            shapes_to_add = shape_ids
        else:
            shapes_to_add = [
                s for s in shape_ids
                if s not in self.shapes_summary.index.unique()
            ]

        if not shapes_to_add:
            return

        # Filter down to just the shapes we need to add
        # TODO: make sure this is handled correctly
        shapes_df = self.shapes[self.shapes['shape_id'].isin(
            shapes_to_add)]
        shapes_multi = shapes_df.set_index(
            ['shape_id', 'shape_pt_sequence'])

        shapes_summary = pd.DataFrame()
        shapes_summary[['start_lat', 'start_lon']] = shapes_multi.groupby(
            'shape_id').apply(lambda x: x.sort_index().iloc[0])[
            ['shape_pt_lat', 'shape_pt_lon']]
        shapes_summary[['end_lat', 'end_lon']] = \
            shapes_multi.groupby('shape_id').apply(
                lambda x: x.sort_index().iloc[-1])[
                ['shape_pt_lat', 'shape_pt_lon']]
        # Calculate distances of all shapes (in miles)
        shape_dists_df = calculate_shape_dists(
            shapes_df=self.shapes, shape_ids=shapes_to_add
        )
        # Add these to the summary DF
        shapes_summary['service_dist'] = shape_dists_df
        # Update the summary df
        if self.shapes_summary is None:
            self.shapes_summary = shapes_summary
        else:
            self.shapes_summary = pd.concat(
                [self.shapes_summary, shapes_summary]
            )

    def get_service_ids_from_date(self, input_date: DatetimeType):
        """
        Get service IDs corresponding to the given input date.

        :param input_date: datetime.datetime object giving specific date
        :return: list of service_ids in service on the given date
        """
        # Convert to Pandas dtype for comparisons below
        input_date = pd.to_datetime(input_date)
        if self.calendar is None:
            ids_cal = list()
        else:
            after_start = input_date >= self.calendar['start_date']
            before_end = input_date <= self.calendar['end_date']
            calendar_filt = self.calendar[(after_start & before_end)]

            dow = input_date.weekday()
            dow_dict = {
                0: 'monday',
                1: 'tuesday',
                2: 'wednesday',
                3: 'thursday',
                4: 'friday',
                5: 'saturday',
                6: 'sunday'
            }
            dow_col = dow_dict[dow]
            calendar_filt = calendar_filt[calendar_filt[dow_col] == 1]

            ids_cal = calendar_filt['service_id'].tolist()

        if self.calendar_dates is None:
            service_add = list()
            service_rmv = list()
        else:
            service_except = self.calendar_dates[
                self.calendar_dates['date'] == input_date]
            if len(service_except) > 0:
                service_add = service_except[
                    service_except['exception_type'] == 1][
                    'service_id'].tolist()
                service_rmv = service_except[
                    service_except['exception_type'] == 2][
                    'service_id'].tolist()

            else:
                service_add = list()
                service_rmv = list()

        # Combine the results
        all_ids = set(
            service_add + [i for i in ids_cal if i not in service_rmv]
        )
            
        if not all_ids:
            warnings.warn(
                'No active service IDs identified on {}'.format(
                    input_date.strftime('%m/%d/%Y')
                )
            )

        return all_ids

    def add_trip_data(
            self, df: pd.DataFrame, ref_date: DatetimeType
        ) -> pd.DataFrame:
        """
        Add relevant details from other GTFS tables to data from trips.txt.

        This function takes as input a DataFrame containing any subset
        of trips as defined in trips.txt and adds the following fields:
            - start_time
            - end_time
            - trip_idx
            - start_lat
            - start_lon
            - end_lat
            - end_lon

        Note that setting trip_idx will NOT work as expected unless
        ALL trips with a given block_id are provided in the input df.
        Otherwise, trip indexes will not be correct.

        :param df: DataFrame containing some subset of block_id values
        :return: DataFrame with fields from other tables added
        """
        if len(df) == 0:
            raise ValueError('Empty DataFrame')
        
        # Convert date to Pandas Timestamp so it can be combined with
        # Timedelta representation of trip start/end times
        ref_date = pd.to_datetime(ref_date)

        # Get stop times only for the relevant trips
        st_filt = self.stop_times.loc[
            self.stop_times['trip_id'].isin(df['trip_id'].tolist()), :
        ]
        st_filt.loc[:, 'arrival_time'] = ref_date \
            + pd.to_timedelta(st_filt['arrival_time'])

        # Get start time of every trip
        start_times = st_filt.loc[
            st_filt.groupby('trip_id')['stop_sequence'].idxmin(),
            ['trip_id', 'arrival_time']].rename(
                columns={'arrival_time': 'start_time'}).set_index('trip_id')
        # Get end time of every trip
        end_times = st_filt.loc[
            st_filt.groupby('trip_id')['stop_sequence'].idxmax(),
            ['trip_id', 'arrival_time']].rename(
                columns={'arrival_time': 'end_time'}).set_index('trip_id')
        # Merge these times and add them to the trips DF
        trip_times = start_times.merge(
            end_times, left_index=True, right_index=True
        )
        trips_mrg = pd.merge(
            df, trip_times, left_on='trip_id', right_index=True
        )
        # Add trip indexes
        trips_mrg = trips_mrg.sort_values(by=['block_id', 'start_time'])
        trips_mrg['trip_idx'] = trips_mrg.groupby('block_id').cumcount() + 1

        # Merge in start/end coords and distance from shapes summary
        # First, we need to ensure the trips are processed in
        # shapes_summary_df to get their coords and distances.
        shape_id_list = list(trips_mrg['shape_id'].unique())
        self.summarize_shapes(shape_ids=shape_id_list)

        trips_mrg = pd.merge(
            trips_mrg, self.shapes_summary, left_on='shape_id',
            right_index=True).reset_index(drop=True)

        return trips_mrg
    
    def get_trips_from_sids(
            self, sids: Iterable, ref_date: DatetimeType=None, add_data=False
        ) -> pd.DataFrame:
        """
        Get all trips with the given service_id value(s)
        :param sids: single service_id or list of service_id values
        :param ref_date: reference date used in time columns
        :param add_data: True if all trip data (e.g. start/end coords,
            stop times, and trip distances) should be added to the
            returned DataFrame
        :return: DataFrame of trip data for matching trips
        """
        # Get only the relevant trips
        trips_filt = self.trips.loc[
            self.trips['service_id'].isin(sids), :
        ]
        # Merge in route data (name, description, and route type)
        trips_mrg = pd.merge(
            trips_filt, self.routes, left_on='route_id', right_index=True)

        if add_data:
            # Get stop times and shape data only for the relevant trips
            trips_mrg = self.add_trip_data(trips_mrg, ref_date)
        
        # If service IDs were supplied and no trips were found, throw a
        # warning
        if sids and len(trips_mrg) == 0:
            warnings.warn(
                'Found no trips matching service IDs: {}. Returning empty '
                'DataFrame.'.format(sids)
            )

        return trips_mrg

    def get_trips_from_date(self, input_date: DatetimeType) -> pd.DataFrame:
        """
        Given a date, gather all needed data on all trips operating.

        :param input_date: date of operation
        :return: dictionary of all relevant trip data
        """
        # Get service IDs operating on the given date
        sids = self.get_service_ids_from_date(input_date)
        # Get only the relevant trips
        trips_out = self.get_trips_from_sids(sids, ref_date=input_date)
        return trips_out

    def get_daily_summary(self) -> pd.Series:
        """
        Calculate the number of active trips each day
        """
        patterns = self.get_service_patterns()
        return patterns.groupby('date')[['n_trips', 'n_blocks']].sum()


    def get_service_patterns(self):
        dow_dict = {
            0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday'
        }

        sid_df = pd.DataFrame(
            self.trips.groupby('service_id')['trip_id'].nunique().rename('n_trips')
        )
        sid_df['n_blocks'] = self.trips.groupby('service_id')['block_id'].nunique()

        if self.calendar is not None:
            cal_df = self.calendar.copy()

            cal_df = cal_df.melt(
                cal_df[['service_id', 'start_date', 'end_date']]
            ).rename({'variable': 'weekday'}, axis=1)
            cal_df = cal_df[cal_df['value'] == 1].drop('value', axis=1)
            # Sometimes, all day values are 0 for some reason. In this case,
            # disregard calendar.txt and move on.
            if cal_df.empty:
                patterns = pd.DataFrame(
                    columns=['date', 'weekday', 'service_id']
                )
            else:
                # Now match up dates and SID values
                patterns = cal_df[['service_id', 'start_date', 'end_date', 'weekday']]
                patterns['date'] = [
                    pd.date_range(s, e, freq='d')
                    for s, e in zip(
                        patterns['start_date'],
                        patterns['end_date'])]
                patterns = patterns.explode('date').drop(['start_date', 'end_date'], axis=1)

                dates_ix = pd.date_range(
                    cal_df['start_date'].min(), cal_df['end_date'].max(), freq='D'
                )

                dates_df = pd.DataFrame(
                    data={
                        'date': dates_ix.to_numpy(),
                        'weekday': dates_ix.dayofweek.to_series().apply(lambda x: dow_dict[x])}
                )

                # Match dates with service IDs
                patterns = pd.merge(dates_df, patterns, on=['date', 'weekday'])

        else:
            patterns = pd.DataFrame(
                columns=['date', 'weekday', 'service_id']
            )

        # Incorporate exceptions from calendar_dates
        if self.calendar_dates is not None:
            cal_dates_df = self.calendar_dates.copy()
            service_add = cal_dates_df[cal_dates_df['exception_type'] == 1].drop(
                'exception_type', axis=1)
            service_rmv = cal_dates_df[cal_dates_df['exception_type'] == 2].drop(
                'exception_type', axis=1)

            # Add service IDs based on calendar_dates
            if len(service_add) > 0:
                service_add['weekday'] = service_add['date'].dt.dayofweek.apply(
                    lambda x: dow_dict[x])
                patterns = pd.concat([patterns, service_add], ignore_index=True)

            # Remove service IDs based on calendar_dates
            for _, row in service_rmv.sort_values(by='date').iterrows():
                match = (patterns['service_id'] == row['service_id']) & (
                        patterns['date'] == row['date'])
                patterns = patterns[~match]

        # Bring in number of trips and blocks based on service IDs
        patterns = pd.merge(patterns, sid_df, on='service_id')

        return patterns
    
    def get_service_pattern_summary(self):
        # Get active service IDs for each day in the feed
        patterns = self.get_service_patterns()
        # Compile these into a set
        dates_to_sids = patterns.groupby('date')['service_id'].apply(frozenset)
        # Define the distinct service patterns (unique sets of service IDs).
        # Generally, most of these will be repeated, so we'll group by pattern
        # rather than every single day in the feed.
        sid_sets = pd.DataFrame(dates_to_sids.unique(), columns=['service_id'])
        sid_sets['pattern'] = 'Service Pattern ' + sid_sets.index.astype(str)
        # Bring the dates back in
        dates_to_patterns = sid_sets.merge(
            dates_to_sids.reset_index(), on='service_id'
        )[['date', 'pattern']].sort_values(by='date')

        # If desired, calculate distance and time of all trips by pulling in
        # data from other files. Use a dummy reference date because we only
        # care about the difference between start and end times for now.
        trips_full = self.add_trip_data(df=self.trips, ref_date='1/1/1970')
        trips_full['service_hours'] = pd.to_timedelta(
            trips_full['end_time'] - trips_full['start_time']
        ).dt.total_seconds() / 3600

        # Compile the number of active trips and blocks per service ID,
        # as well as the total distance and time in service.
        service_cts = trips_full.groupby('service_id').agg(
            {
                'trip_id': 'nunique',
                'block_id': 'nunique',
                'service_dist': 'sum',
                'service_hours': 'sum'
            }
        )

        # Compile the number of trips and blocks per pattern, plus total
        # distance and time in service
        pattern_summary = sid_sets.explode('service_id').merge(
            service_cts,
            left_on='service_id',
            right_index=True
        ).groupby('pattern')[
            ['trip_id', 'block_id', 'service_dist', 'service_hours']
        ].sum().rename(
            columns={'trip_id': 'n_trips', 'block_id': 'n_blocks'}
        )

        # Merge in number of dates that follow each pattern
        pattern_summary = pattern_summary.merge(
            dates_to_patterns.groupby('pattern')['date'].nunique().rename('n_dates'),
            left_index=True, right_index=True
        ).sort_values(by='n_dates', ascending=False)
        return pattern_summary

