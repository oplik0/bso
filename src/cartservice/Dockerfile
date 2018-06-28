FROM gcr.io/google-appengine/aspnetcore:2.1.0
RUN apt update && apt install net-tools telnet
WORKDIR /app
COPY . .
RUN dotnet restore && \
    dotnet build && \
    dotnet publish
WORKDIR /app/bin/Debug/netcoreapp2.0
ENV PORT 7070
EXPOSE 7070
ENTRYPOINT ["dotnet", "cartservice.dll", "start"]
