import subprocess
import sys
import os

generator, \
    generator_tag, \
    openapi_file, \
    openapi_url, \
    config_file, \
    template_dir, \
    *args = sys.argv[1:]

cmd = "docker run -u 1001 --rm --workdir /github/workspace"
cmd = f"{cmd} -v {os.getenv('GITHUB_WORKSPACE')}:/github/workspace"
cmd = f"{cmd} openapitools/openapi-generator-cli:{generator_tag} generate"
cmd = f"{cmd} -g {generator} -o /github/workspace/{generator}-client"

if openapi_url == "UNSET":
    if not openapi_file.startswith("/"):
        openapi_file = f"/github/workspace/{openapi_file}"
    cmd += f" -i {openapi_file}"
else:
    cmd += f" -i {openapi_url}"

if config_file != "UNSET":
    if not config_file.startswith("/"):
        config_file = f"/github/workspace/{config_file}"
    cmd += f" -c {config_file}"

if template_dir != "UNSET":
    if not template_dir.startswith("/"):
        template_dir = f"/github/workspace/{template_dir}"
    cmd += f" -t {template_dir}"

if args:
    cmd += f" {' '.join(args)}"

# Call the command and return the exit code
exit_code = subprocess.call(cmd, shell=True)
sys.exit(exit_code)
