# Use the official Apache Flink image
FROM flink:latest

# Expose necessary ports
EXPOSE 8081 6123 6124 8082

# Set the working directory
WORKDIR /opt/flink

# Start Flink in standalone mode
CMD ["bin/jobmanager.sh", "start-foreground"]
