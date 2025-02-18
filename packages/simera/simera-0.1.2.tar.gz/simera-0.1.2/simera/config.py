from pathlib import Path


class SimeraConfig:
    def __init__(self, resources_path=None):
        self.path = self._Path(resources_path)

    class _Path:

        def __init__(self, resources_path):
            self.base_dir = Path().cwd()
            self.resources = self.base_dir / 'simera_resources' if resources_path is None else resources_path
            self.mapping = self.resources / 'mapping'
            self.transport = self.resources / 'transport'
            self.warehouse = self.resources / 'warehouse'

            self.file_master_mapper = self.mappings / 'master_mapper.xlsb'
