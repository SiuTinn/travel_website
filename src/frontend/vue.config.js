const webpack = require('webpack');
const isProd = process.env.NODE_ENV === "production";

module.exports = {
    publicPath: isProd ? "/vue-argon-dashboard/" : "",
    configureWebpack: {
        // Set up all the aliases we use in our app.
        plugins: [
            new webpack.optimize.LimitChunkCountPlugin({
                maxChunks: 6
            })
        ]
    },
    devServer: {
        host: 'localhost',      // 避免 sockjs 指到 10.135.2.116
        port: 8080,
        proxy: {
          '/api': {
            target: 'http://localhost:8000', // Django 本地地址
            changeOrigin: true
          }
        }
      },
    pwa: {
        name: 'Vue Argon Dashboard',
        themeColor: '#172b4d',
        msTileColor: '#172b4d',
        appleMobileWebAppCapable: 'yes',
        appleMobileWebAppStatusBarStyle: '#172b4d'
    },
    css: {
        // Enable CSS source maps.
        sourceMap: process.env.NODE_ENV !== 'production'
    }
};
