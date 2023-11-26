# Use a base image with build tools
FROM kalilinux/kali-rolling AS builder

# Set the working directory
WORKDIR /app

# Copy the source code
COPY buffer_overflow_challenge.c .

# Build the binary with debugging symbols
RUN apt-get update && apt-get install -y gcc \
    && gcc -g -o buffer_overflow_challenge buffer_overflow_challenge.c -fno-stack-protector -z execstack

# Create a smaller final image
FROM kalilinux/kali-rolling

# Set the working directory
WORKDIR /app

# Copy the compiled binary from the builder image
COPY --from=builder /app/buffer_overflow_challenge /app/buffer_overflow_challenge

# Set permissions if needed
RUN chmod +x /app/buffer_overflow_challenge

# Expose any necessary ports (if applicable)
# EXPOSE 1234

# Run the command to start your challenge
CMD ["/app/buffer_overflow_challenge"]

