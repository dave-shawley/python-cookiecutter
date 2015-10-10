try:
    from {{cookiecutter.project_name}}.app import run
except ImportError as exc:
    def run(*args, **kwargs):
        raise exc

version_info = (0, 0, 0)
__version__ = '.'.join(str(v) for v in version_info[:3])

__all__ = ('run', '__version__', 'version_info')
