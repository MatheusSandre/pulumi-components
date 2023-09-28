import os
import json
import jinja2

class FileLoader:
    @staticmethod
    def file_dir_compose(file_dir):
        staging_environments = ["qa", "next"]
        if os.environ['PULUMI_STACK'] == "qa-devs":
            folder = os.environ['PULUMI_STACK']
        elif any(env in str(os.environ['PULUMI_STACK']) for env in staging_environments):
            folder = "qa"
        else:
            folder = os.environ['PULUMI_STACK']

        return f"{file_dir}{folder}/"

    @staticmethod
    def start_from_json(file_dir, name, separator_enabled):
        with open(f"{file_dir}/{name}.json", 'r', encoding="utf-8") as file:
            if separator_enabled:
                data = json.loads(file.read())
                return json.dumps(data, separators=(",", ":"))

            data = file.read()
            return json.loads(data)

    @staticmethod
    def start_from_template(file_dir, envs, template_file, separator_enabled, file_type):
        file_path = f"{file_dir}/"
        if file_type == "JSON":
            creater = jinja2.Environment(loader=jinja2.FileSystemLoader(file_path)).get_template(f"{template_file}.json")
            file = creater.render(environs=envs)
            if separator_enabled:
                data = json.loads(file)
                return json.dumps(data, separators=(",", ":"))

            return json.loads(file)
        if file_type == "YML":
            creater = jinja2.Environment(loader=jinja2.FileSystemLoader(file_path)).get_template(f"{template_file}.yml")
            file = creater.render(environs=envs)
            return file

        raise Exception("Sorry, only support JSON or YML")
