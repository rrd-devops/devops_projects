FROM nginx:alpine
# copy index.html into the default nginx html folder
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]
