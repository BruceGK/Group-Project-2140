# 1. build frontend code
# FROM node:14.16.0 AS build-stage
# COPY . .
# RUN rm -rf node_modules
# RUN yarn
# RUN yarn build

# 2. start nginx server to serve static files
FROM nginx AS serve-stage
# COPY --from=build-stage /build/ /usr/share/nginx/html
# COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
