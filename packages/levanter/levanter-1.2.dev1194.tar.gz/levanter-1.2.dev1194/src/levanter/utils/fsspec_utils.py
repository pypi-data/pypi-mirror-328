import braceexpand
import fsspec
from fsspec.asyn import AsyncFileSystem


def exists(url, **kwargs) -> bool:
    """Check if a file exists on a remote filesystem."""
    fs, path = fsspec.core.url_to_fs(url, **kwargs)
    return fs.exists(path)


def mkdirs(path):
    """Create a directory and any necessary parent directories."""
    fs, path = fsspec.core.url_to_fs(path)
    fs.makedirs(path, exist_ok=True)


def expand_glob(url):
    expanded_urls = braceexpand.braceexpand(url)
    for expanded_url in expanded_urls:
        if "*" in expanded_url:
            fs = fsspec.core.url_to_fs(expanded_url)[0]
            globbed = fs.glob(expanded_url)
            # have to append the fs prefix back on
            protocol, _ = fsspec.core.split_protocol(expanded_url)
            if protocol is None:
                yield from globbed
            else:
                yield from [f"{protocol}://{path}" for path in globbed]
        else:
            yield expanded_url


def remove(url, *, recursive=False, **kwargs):
    """Remove a file from a remote filesystem."""
    # TODO: better to use a STS deletion policy or job for this one.
    fs, path = fsspec.core.url_to_fs(url, **kwargs)

    fs.rm(path, recursive=recursive)


async def async_remove(url, *, recursive=False, **kwargs):
    """Remove a file from a remote filesystem."""
    fs, path = fsspec.core.url_to_fs(url, **kwargs)

    if isinstance(fs, AsyncFileSystem):
        return await fs._rm(path, recursive=recursive)
    else:
        fs.rm(path, recursive=recursive)
