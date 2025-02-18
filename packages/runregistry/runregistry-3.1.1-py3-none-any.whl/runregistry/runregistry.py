import os
import sys
import time
import json
import requests
from dotenv import load_dotenv
from cernrequests import get_api_token
from runregistry.utils import (
    transform_to_rr_run_filter,
    transform_to_rr_dataset_filter,
    __parse_runs_arg,
)

__version__ = "3.1.1"

# Look for .env file in the directory of the caller
# first. If it exists, use it.
if os.path.exists(os.path.join(os.getcwd(), ".env")):
    load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
else:
    load_dotenv()


# Silence unverified HTTPS warning:
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PAGE_SIZE = 50

# Offline table
WAITING_DQM_GUI_CONSTANT = "waiting dqm gui"

# Valid Lumisection statuses
LUMISECTION_STATES = ["GOOD", "BAD", "STANDBY", "EXCLUDED", "NOTSET"]

ONLINE_RUN_STATES = ["SIGNOFF", "OPEN", "COMPLETED"]

OFFLINE_DATASET_STATES = ["SIGNOFF", "OPEN", "COMPLETED", WAITING_DQM_GUI_CONSTANT]

# Time to sleep between JSON creation checks
JSON_CREATION_SLEEP_TIME = 15

staging_cert = ""
staging_key = ""
api_url = ""
use_cookies = True
email = "api@api"
client_id = os.environ.get("SSO_CLIENT_ID")
client_secret = os.environ.get("SSO_CLIENT_SECRET")
target_application = ""
target_name = ""


def setup(target):
    global api_url
    global target_application
    global use_cookies
    global target_name

    if target == "local":
        api_url = "http://localhost:9500"
        use_cookies = False
        target_application = ""
    elif target == "development":
        api_url = "https://dev-cmsrunregistry.web.cern.ch/api"
        use_cookies = True
        target_application = "dev-cmsrunregistry-sso-proxy"
    elif target == "production":
        api_url = "https://cmsrunregistry.web.cern.ch/api"
        use_cookies = True
        target_application = "cmsrunregistry-sso-proxy"
    else:
        raise Exception(
            f'Invalid setup target "{target}". Valid options: "local", "development", "production".'
        )
    target_name = target


def _get_user_agent():
    return f"runregistry_api_client/{__version__} ({_get_target()}, python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}, requests {requests.__version__})"


def _get_headers(token: str = ""):
    headers = {"Content-type": "application/json"}
    if not use_cookies:
        headers["email"] = email
    if token:
        headers["Authorization"] = "Bearer " + token
    headers["User-Agent"] = _get_user_agent()
    return headers


setup(os.environ.get("ENVIRONMENT", "production"))


def _get_target():
    return target_name


def _get_token():
    """
    Gets the token required to query RR API through the CERN SSO.
    :return: the token required to query Run Registry API.
    """
    if _get_target() == "local":
        return ""
    token, expiration_date = get_api_token(
        client_id=client_id,
        client_secret=client_secret,
        target_application=target_application,
    )
    return token


def _get_page(
    url, page=0, data_type="runs", ignore_filter_transformation=False, **kwargs
):
    """
    :param ignore_filter_transformation: If user knows how the filter works (by observing http requests on RR website), and wants to ignore the suggested transformation to query API, user can do it by setting ignore_filter_transformation to True
    :param filter: The filter to be transformed into RR syntax, and then sent for querying
    :return: A page in Run registry
    """
    headers = _get_headers(token=_get_token())
    query_filter = kwargs.pop("filter", {})
    if data_type == "runs" and not ignore_filter_transformation:
        query_filter = transform_to_rr_run_filter(run_filter=query_filter)
    elif data_type == "datasets" and not ignore_filter_transformation:
        query_filter = transform_to_rr_dataset_filter(dataset_filter=query_filter)
    if _get_target() in ["development", "local"]:
        print(url)
        print(query_filter)
    payload = json.dumps(
        {
            "page": page,
            "filter": query_filter,
            "page_size": kwargs.pop("page_size", PAGE_SIZE),
            "sortings": kwargs.pop("sortings", []),
        }
    )

    return requests.post(url, headers=headers, data=payload).json()


def get_dataset_names_of_run(run_number, **kwargs):
    """
    Gets the existing dataset names of a run_number
    :return: Array of dataset names of the specified run_number
    """
    url = "{}/get_all_dataset_names_of_run/{}".format(api_url, run_number)
    return requests.get(url, headers=_get_headers(token=_get_token())).json()


def get_run(run_number, **kwargs):
    """
    Gets all the info about a particular run
    :param run_number: run_number of specified run
    """
    run = get_runs(filter={"run_number": run_number}, **kwargs)
    if not run:
        return {}
    if len(run) > 1:
        raise Exception(
            f"Unexpected number of results returned for run {run_number} ({len(run)}), was expecting exactly 1"
        )
    return run[0]


def get_runs(limit=40000, compress_attributes=True, **kwargs):
    """
    Gets all runs that match the filter given in
    :param compress_attributes: Gets the attributes inside rr_attributes:* and the ones in the DatasetTripletCache (The lumisections insdie the run/dataset) and spreads them over the run object
    :param filter: the filter applied to the runs needed
    """
    url = "{}/runs_filtered_ordered".format(api_url)
    initial_response = _get_page(url=url, data_type="runs", page=0, **kwargs)
    if "err" in initial_response:
        raise ValueError(initial_response["err"])

    resource_count = initial_response["count"]
    page_count = initial_response["pages"]
    runs = initial_response["runs"]
    if resource_count > limit:
        print(
            "ALERT: The specific run registry api request returns more runs than the limit({}), consider passing a greater limit to get_runs(limit=number) to get the whole result.".format(
                limit
            )
        )
    if resource_count > 10000:
        print(
            "WARNING: fetching more than 10,000 runs from run registry. you probably want to pass a filter into get_runs, or else this will take a while."
        )
    if resource_count > 20000 and "filter" not in kwargs:
        raise Exception(
            "ERROR: For run registry queries that retrieve more than 20,000 runs, you must pass a filter into get_runs, an empty filter get_runs(filter={}) works"
        )
    for page_number in range(1, page_count):
        additional_runs = _get_page(
            page=page_number, url=url, data_type="runs", **kwargs
        )
        runs.extend(additional_runs.get("runs"))
        if len(runs) >= limit:
            runs = runs[:limit]
            break

    if compress_attributes:
        compressed_runs = []
        for run in runs:
            compressed_run = {
                "oms_attributes": run["oms_attributes"],
                **run["rr_attributes"],
                "lumisections": run["DatasetTripletCache"]["triplet_summary"],
                **run,
            }
            del compressed_run["rr_attributes"]
            del compressed_run["DatasetTripletCache"]
            compressed_runs.append(compressed_run)
        return compressed_runs

    return runs


def get_dataset(run_number, dataset_name="online", **kwargs):
    """
    Gets information about the dataset specified by run_number and dataset_name
    :param run_number:  The run number of the dataset
    :param dataset_name: The name of the dataset. 'online' is the dataset of the online run. These are Run Registry specific dataset names e.g. online, /PromptReco/Collisions2018D/DQM, /Express/Collisions2018/DQM
    """
    dataset = get_datasets(
        filter={"run_number": run_number, "dataset_name": dataset_name}, **kwargs
    )
    if not dataset:
        return {}
    if len(dataset) > 1:
        raise Exception(
            f"Unexpected number of results returned for dataset {dataset_name} of run {run_number} ({len(dataset)}), was expecting exactly 1"
        )
    return dataset[0]


def get_datasets(limit=40000, compress_attributes=True, **kwargs) -> list:
    """
    Gets all datasets that match the filter given
    :param compress_attributes: Gets the attributes inside rr_attributes:* and the ones in the DatasetTripletCache (The lumisections insdie the run/dataset) and spreads them over the run object
    """
    url = "{}/datasets_filtered_ordered".format(api_url)
    initial_response = _get_page(url=url, data_type="datasets", page=0, **kwargs)
    if "err" in initial_response:
        raise ValueError(initial_response["err"])

    resource_count = initial_response["count"]
    page_count = initial_response["pages"]
    datasets = initial_response["datasets"]
    if resource_count > limit:
        print(
            "ALERT: The specific api request returns more datasets than the limit({}), consider passing a greater limit to get_datasets(limit=number) to get the whole result.".format(
                limit
            )
        )
    if resource_count > 10000:
        print(
            "WARNING: fetching more than 10,000 datasets. you probably want to pass a filter into get_datasets, or else this will take a while."
        )
    if resource_count > 20000 and "filter" not in kwargs:
        raise Exception(
            "ERROR: For queries that retrieve more than 20,000 datasets, you must pass a filter into get_datasets, an empty filter get_datasets(filter={}) works"
        )
    for page_number in range(1, page_count):
        additional_datasets = _get_page(
            page=page_number, url=url, data_type="datasets", **kwargs
        )
        datasets.extend(additional_datasets.get("datasets"))
        if len(datasets) >= limit:
            datasets = datasets[:limit]
            break

    if compress_attributes:
        compressed_datasets = []
        for dataset in datasets:
            compressed_dataset = {
                **dataset["Run"]["rr_attributes"],
                **dataset,
                "lumisections": dataset["DatasetTripletCache"]["triplet_summary"],
            }
            del compressed_dataset["DatasetTripletCache"]
            del compressed_dataset["Run"]
            compressed_datasets.append(compressed_dataset)
        return compressed_datasets
    return datasets


def get_cycles():
    url = "{}/cycles/global".format(api_url)
    headers = _get_headers(token=_get_token())
    if _get_target() in ["development", "local"]:
        print(url)
    return requests.get(url, headers=headers).json()


def _get_lumisection_helper(url, run_number, dataset_name="online", **kwargs):
    """
    Puts the headers and POST data for all other lumisection methods
    """

    headers = _get_headers(token=_get_token())
    payload = json.dumps({"run_number": run_number, "dataset_name": dataset_name})
    return requests.post(url, headers=headers, data=payload).json()


def get_lumisections(run_number, dataset_name="online", **kwargs):
    """
    Gets the Run Registry lumisections of the specified dataset
    """
    url = "{}/lumisections/rr_lumisections".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name, **kwargs)


def get_oms_lumisections(run_number, dataset_name="online", **kwargs):
    """
    Gets the OMS lumisections saved in RR database
    """
    url = "{}/lumisections/oms_lumisections".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name, **kwargs)


def get_lumisection_ranges(run_number, dataset_name="online", **kwargs):
    """
    Gets the lumisection ranges of the specified dataset. Returns
    a list of dicts, each one containing a lumisection "range", dictated
    by the 'start' and 'stop' keys of the dict. In the same dict,
    the status, cause, and comments per component are found.
    """
    url = "{}/lumisections/rr_lumisection_ranges".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name, **kwargs)


def get_lumisection_ranges_by_component(run_number, dataset_name="online", **kwargs):
    """
    Gets the lumisection ranges of the specified dataset as a dict,
    where the components are the keys (e.g. 'rpc-rpc'). Each dict value is
    a list of lumisection "ranges" (dicts) for the specific component. The exact
    range is dictated by the 'start' and 'stop' keys of the nested dict.

    Similar to get_lumisection_ranges, but organized by component.
    """
    url = "{}/lumisections/rr_lumisection_ranges_by_component".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name, **kwargs)


def get_oms_lumisection_ranges(run_number, **kwargs):
    """
    Gets the OMS lumisection ranges of the specified dataset (saved in RR database)
    """
    url = "{}/lumisections/oms_lumisection_ranges".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name="online", **kwargs)


def get_joint_lumisection_ranges(run_number, dataset_name="online", **kwargs):
    """
    Gets the lumisection ranges of the specified dataset, breaken into RR breaks and OMS ranges
    """
    url = "{}/lumisections/joint_lumisection_ranges".format(api_url)
    return _get_lumisection_helper(url, run_number, dataset_name, **kwargs)


# Using json portal (safe):
def create_json(json_logic, dataset_name_filter, **kwargs):
    """
    It adds a json to the queue and polls until json is either finished or an error occured
    """
    if not isinstance(json_logic, str):
        json_logic = json.dumps(json_logic)
    url = "{}/json_portal/generate".format(api_url)

    headers = _get_headers(token=_get_token())
    payload = json.dumps(
        {"json_logic": json_logic, "dataset_name_filter": dataset_name_filter}
    )
    response = requests.post(url, headers=headers, data=payload).json()

    # Id of json:
    id_json = response["id"]
    # Poll JSON until job is complete
    while True:
        # polling URL:
        url = "{}/json_portal/json".format(api_url)

        headers = _get_headers(token=_get_token())

        payload = json.dumps({"id_json": id_json})
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()["final_json"]
        elif response.status_code == 202:
            # stil processing
            print(f"progress creating json: {response.json()['progress']}")
            time.sleep(JSON_CREATION_SLEEP_TIME)
        elif response.status_code == 203:
            # stil processing
            print("json process is submited and pending, please wait...")
            time.sleep(JSON_CREATION_SLEEP_TIME)
        else:
            raise Exception(
                f"Error {response.status_code} during JSON creation: {response.text}"
            )


def get_datasets_accepted():
    """
    Method for fetching current datasets accepted in Offline Run Registry
    """
    url = "{}/datasets_accepted".format(api_url)
    headers = _get_headers(token=_get_token())
    return requests.get(url, headers=headers).json()


# advanced RR operations ==============================================================================
# Online Table
def move_runs(from_, to_, run=None, runs=[], **kwargs):
    """
    move run/runs from one state to another
    """
    if not run and not runs:
        raise ValueError("move_runs(): no 'run' and 'runs' arguments were provided")

    if from_ not in ONLINE_RUN_STATES or to_ not in ONLINE_RUN_STATES:
        raise ValueError(
            f"move_runs(): got states '{from_}, '{to_}'",
            f" but allowed states are {ONLINE_RUN_STATES}",
        )

    url = "%s/runs/move_run/%s/%s" % (api_url, from_, to_)

    headers = _get_headers(token=_get_token())

    if run:
        runs = [run]

    answers = []
    for run_number in runs:
        payload = json.dumps({"run_number": run_number})
        answer = requests.post(url, headers=headers, data=payload)
        if answer.status_code != 200:
            raise Exception(
                f"Got response {answer.status_code} when moving datasets: {answer.text}"
            )
        answers.append(answer.json())

    return answers


def make_significant_runs(run=None, runs=[], **kwargs):
    """
    mark run/runs significant
    """
    if not run and not runs:
        raise ValueError(
            "make_significant_runs(): no 'run' and 'runs' arguments were provided"
        )

    url = "%s/runs/mark_significant" % (api_url)
    headers = _get_headers(token=_get_token())

    if run:
        runs = [run]

    answers = []
    for run_number in runs:
        data = {"run_number": run}
        answer = requests.post(url, headers=headers, json=data)
        if answer.status_code != 200:
            raise Exception(
                f"Got response {answer.status_code} when making runs significant: {answer.text}"
            )
        answers.append(answer.json())

    return answers


def reset_RR_attributes_and_refresh_runs(runs=[], **kwargs):
    """
    reset RR attributes and refresh run/runs
    """
    runs = __parse_runs_arg(runs)
    if not runs:
        raise ValueError(
            "reset_RR_attributes_and_refresh_runs(): no 'runs' argument was provided"
        )
    headers = _get_headers(token=_get_token())
    answers = []
    for run_number in runs:
        url = "%s/runs/reset_and_refresh_run/%d" % (api_url, run_number)
        answer = requests.post(url, headers=headers)
        if answer.status_code != 200:
            raise Exception(
                f"Got response {answer.status_code} when resetting and refreshing runs: {answer.text}"
            )
        answers.append(answer.json())

    return answers


def manually_refresh_components_statuses_for_runs(runs=[], **kwargs):
    """
    Refreshes all components statuses for the runs specified that have not been
    changed by shifters.
    """
    runs = __parse_runs_arg(runs)

    if not runs:
        raise ValueError(
            "manually_refresh_components_statuses_for_runs(): no 'runs' argument was provided"
        )

    headers = _get_headers(token=_get_token())
    answers = []
    for run_number in runs:
        url = "%s/runs/refresh_run/%d" % (api_url, run_number)
        answer = requests.post(url, headers=headers)
        if answer.status_code != 200:
            raise Exception(
                f"Got response {answer.status_code} when manually refreshing component statuses: {answer.text}"
            )
        answers.append(answer.json())

    return answers


def edit_rr_lumisections(
    run,
    lumi_start,
    lumi_end,
    component,
    status,
    comment="",
    cause="",
    dataset_name="online",
    **kwargs,
):
    """
    WIP edit RR lumisections attributes
    """
    if status not in LUMISECTION_STATES:
        raise ValueError(
            f"edit_rr_lumisections(): got status '{status}'",
            f" but allowed statuses are {LUMISECTION_STATES}",
        )

    url = "%s/lumisections/edit_rr_lumisections" % (api_url)

    headers = _get_headers(token=_get_token())
    payload = json.dumps(
        {
            "new_lumisection_range": {
                "start": lumi_start,
                "end": lumi_end,
                "status": status,
                "comment": comment,
                "cause": cause,
            },
            "run_number": run,
            "dataset_name": dataset_name,
            "component": component,
        }
    )
    answer = requests.put(url, headers=headers, data=payload)
    if answer.status_code != 200:
        raise Exception(
            f"Got response {answer.status_code} when editing rr lumisections: {answer.text}"
        )
    return answer.json()


def move_datasets(
    from_, to_, dataset_name, workspace="global", run=None, runs=[], **kwargs
):
    """
    Move offline dataset/datasets from one state to another.
    Requires a privileged token.
    """
    if not run and not runs:
        raise ValueError("move_datasets(): no 'run' and 'runs' arguments were provided")

    if from_ not in OFFLINE_DATASET_STATES or to_ not in OFFLINE_DATASET_STATES:
        raise ValueError(
            f"move_datasets(): got states '{from_}', '{to_}",
            f" but allowed states are {OFFLINE_DATASET_STATES}",
        )

    url = "%s/datasets/%s/move_dataset/%s/%s" % (api_url, workspace, from_, to_)

    headers = _get_headers(token=_get_token())

    if run:
        runs = [run]

    answers = []
    for run_number in runs:
        payload = json.dumps(
            {
                "run_number": run_number,
                "dataset_name": dataset_name,
                "workspace": workspace,
            }
        )
        answer = requests.post(url, headers=headers, data=payload)
        if answer.status_code != 200:
            raise Exception(
                f"Got response {answer.status_code} when moving datasets: {answer.text}"
            )
        answers.append(answer.json())

    return answers


def change_run_class(run_numbers, new_class):
    """
    Method for changing the class of a run (or runs),
    e.g. from "Commissioning22" to "Cosmics22".
    Requires a privileged token.
    """
    headers = _get_headers(token=_get_token())

    def _execute_request_for_single_run(run_number, new_class):
        payload = json.dumps({"class": new_class})
        return requests.put(
            url="%s/manual_run_edit/%s/class" % (api_url, run_number),
            headers=headers,
            data=payload,
        )

    if not isinstance(new_class, str):
        raise ValueError(f'Invalid input "{new_class}" for "new_class"')
    answers = []
    # If just one int provided, make it into a list
    if isinstance(run_numbers, int):
        run_numbers = [run_numbers]

    if isinstance(run_numbers, list):
        for run_number in run_numbers:
            if not isinstance(run_number, int):
                raise ValueError(
                    "Invalid run number value found in run_numbers. Please provide a list of numbers."
                )
            answer = _execute_request_for_single_run(run_number, new_class)
            if answer.status_code != 200:
                raise Exception(
                    f"Got response {answer.status_code} when changing run class: {answer.text}"
                )
            answers.append(answer.json())
    else:
        raise ValueError(
            'Invalid input for "run_numbers". Please provide a list of numbers.'
        )
    return answers
