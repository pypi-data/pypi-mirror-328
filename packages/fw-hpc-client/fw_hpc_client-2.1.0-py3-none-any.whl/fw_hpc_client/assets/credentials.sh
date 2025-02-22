
# Cast bash configuration and credentials
# Contact: <Your-Email-Here>

# The engine defaults to a folder in /opt for its state.
# For HPC this is likely unavailable.
# Ideally, set this to a user-specific dir, such as "/tmp/<Your-User>"
export ENGINE_CACHE_DIR="/some-folder"
export ENGINE_TEMP_DIR="/some-folder"

# Flywheel SDK settings
export FLYWHEEL_SDK_SKIP_VERSION_CHECK="1"

# Flywheel site credentials. SCITRAN_RUNTIME_HOST is your flywheel site URL (e.g.,
# `ga.ce.flywheel.io`). Do not use the scheme portion of your URL (e.g., `https://`),
# or subdirectories (e.g., `#/projects`), only domains. SCITRAN_CORE_DRONE_SECRET will
# be provided by flywheel support staff.
export SCITRAN_RUNTIME_HOST="<your-flyhwheel-site-domain>"
export SCITRAN_RUNTIME_PORT="443"
export SCITRAN_CORE_DRONE_SECRET="<your-credentials>"

# Disable metrics server
export ENGINE_METRICS_PORT=-1

# Enable signed URLs
export ENGINE_SIGNED_URLS=1

# HPC compatible compute
export ENGINE_MODULE=singularity

# absolute path to the singularity executable
export PATH=$PATH:/usr/local/bin/

# singularity working directory for /tmp, /var/tmp, and $HOME. Default is the OS `tmp`
# directory
# export SINGULARITY_WORKDIR="path/to/singularity_workdir"

# "SingularityCE will cache SIF container images generated from remote sources, and any
# OCI/docker layers used to create them". The default is $HOME/.singularity/cache
# export SINGULARITY_CACHEDIR="path/to/singularity/cache"

# Use SINGULARITY_BIND if you would like to mount an additional directory to the
# singularity image/SIF file. This can be useful if you would like to use a writable
# directory for creating temporary files instead of generating them in the default /tmp
# directory.
# The argument for this option is a comma-delimited string of bind path specifications in the format src[:dest[:opts]],
# where src and dest are paths outside and inside the container, respectively. If dest is not given, it is set equal to src. Mount options
# (opts) may be specified as ro (read-only) or rw (read/writ, which is the default). A comma-delimited string of bind path specifications can be used.
# export SINGULARITY_BIND="/scratch/oa22/fmripreptempdir"

# Do NOT put other engine settings in this file.
