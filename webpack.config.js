var path = require('path');
var webpack = require('webpack');
// var BundleTracker = require('webpack-bundle-tracker');
const autoprefixer = require('autoprefixer');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
module.exports = {
  mode: 'development',
  context: __dirname,
  entry: {
    main:'./src/app.scss',
    app:'./src/index.js',
    vendor:['vue']
  },
  output: {
      path: path.resolve(__dirname, './src/output'),
      filename: "[name].js"
  },
  module: {
  	rules: [
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'main.css',
            },
          },
          {loader: 'extract-loader'},
          {loader: 'css-loader'},
          {
            loader: 'postcss-loader',
            options: {
              plugins: () => [autoprefixer()]
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  plugins:[
      new VueLoaderPlugin()
  ]
};