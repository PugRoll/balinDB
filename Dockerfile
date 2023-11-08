#Use a base image
FROM archlinux:base


#Update the system and install SQLite
RUN pacman -Syu --noconfirm && \
    pacman -S sqlite python python-pip python-flask --noconfirm



WORKDIR /app

#Copy pre-populated SQLite database into the container


#Copy .tar.gz file into the container
COPY balinAdd.tar.gz /app/balinAdd.tar.gz
COPY balinSubtract.tar.gz /app/balinSubtract.tar.gz


COPY init-db.sh /app/init-db.sh
COPY init.sql /app/init.sql

EXPOSE 5000

COPY convertToBlob.py /app/convertToBlob.py
COPY ./app.py /app/app.py



RUN chmod +x /app/init-db.sh

CMD ["/app/init-db.sh"]
