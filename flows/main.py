from prefect import flow, task, get_run_logger
from platform import node, platform
from sub import sub

@task(log_prints=True)
def subflow():
    return 'Sub-flow is running well.'

@flow(log_prints=True)
def main(user_input: str = "World"):
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 🚀", user_input)
    logger.info("Network: %s. Instance: %s. Agent is healthy ✅️", node(), platform())
    print(subflow())


if __name__ == "__main__":
    main()
