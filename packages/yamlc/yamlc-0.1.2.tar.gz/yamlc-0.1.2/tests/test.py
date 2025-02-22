from yamlc import Yamlc

Yamlc.set_config_file_path("config.yaml")

print(Yamlc.get("app.name"))
print(Yamlc.get("api.base_url"))
