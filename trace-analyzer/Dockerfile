# We use a multi-stage build to avoid having to install Rust nad Rye in the final image
FROM rust:alpine3.20 as rye_setup

# Start by installing the Rye CLI
RUN cargo install --git https://github.com/mitsuhiko/rye rye

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV RYE_HOME="/app/rye"
ENV PATH="$RYE_HOME/shims:/usr/local/cargo/bin/:$PATH"

# Install dependencies first, so that this layer will be cached even if the code changes
COPY pyproject.toml .
RUN rye self install --yes && \
    rye sync

# Now we can build the application
COPY . .
RUN rye build --wheel --clean

# Now we can build the final minimal image
FROM python:alpine3.20 as run

# Install the built wheel, without even copying it to the final image
RUN --mount=type=bind,from=build,source=/app/dist,target=/dist PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir /dist/*.whl

# Our application is just a Python module, so we can run it like this
CMD python -m trace_analyzer