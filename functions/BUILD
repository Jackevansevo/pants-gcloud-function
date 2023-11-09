python_sources()

pex_binary(
    name="flask",
    entry_point="flask",
    dependencies=["./main.py", ":reqs#python-dotenv"],
)

python_google_cloud_function(
    name="cloud_function",
    handler="main.py:handler",
    type="http",
    runtime="python311",
)

python_requirements(
    name="reqs",
)
