

def validate_manifest(data, validator, error):
    import os.path
    schema_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'manifest-schema.yml'))
    validator(data, schema_path)


def resolve_tasks(taskset, manifest):
    from bootstrapvz.common.tasks import ssh
    from tasks import SetRootPassword
    taskset.discard(ssh.DisableSSHPasswordAuthentication)
    taskset.add(ssh.EnableRootLogin)
    taskset.add(SetRootPassword)
