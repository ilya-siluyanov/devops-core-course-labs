ARG TARGET_PLATFORM=x86_64-unknown-linux-musl

FROM rust:1.72-slim-buster as builder
ARG TARGET_PLATFORM

RUN cargo new app_rust
ARG RUSTFLAGS=''
RUN rustup target add ${TARGET_PLATFORM}

WORKDIR /app_rust

COPY Cargo.toml Cargo.lock ./

COPY src src
RUN RUSTFLAGS=${RUSTFLAGS} cargo build --target ${TARGET_PLATFORM}

FROM alpine:3.18.3
ARG TARGET_PLATFORM

RUN apk --no-cache  update && \
   apk add --no-cache curl && \
   rm -rf /var/cache/apk/*


WORKDIR /
COPY --from=builder /app_rust/target/${TARGET_PLATFORM}/debug/app_rust app_rust
RUN chmod -R a-w+rx app_rust && adduser -DHs /bin/bash devuser
USER devuser

EXPOSE 8000

HEALTHCHECK CMD curl -f localhost:8000/health || exit 1
ENTRYPOINT ["./app_rust"]
