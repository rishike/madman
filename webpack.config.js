var path = require('path');
var webpack = require('webpack');
// var BundleTracker = require('webpack-bundle-tracker');
const autoprefixer = require('autoprefixer');

module.exports = {
  mode: 'development',
  context: __dirname,
  entry: ['./src/app.scss','./src/index.js'],
  output: {
      path: path.resolve(__dirname, './src/output'),
      filename: "bundle.js"
  },
  module: {
  	rules: [
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'bundle.css',
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
      }
    ]
  },
  plugins:[

  ]
};