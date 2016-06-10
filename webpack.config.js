/*
* @Author: Marcela Campo
* @Date:   2016-05-29 20:08:37
* @Last Modified by:   Marcela Campo
* @Last Modified time: 2016-05-30 01:20:52
*/

  module.exports = {
     entry: './src/ui/app.js',
     output: {
         path: './static/scripts',
         filename: 'app.bundle.js',
     },
     module: {
         loaders: [{
             test: /\.js$/,
              exclude: /node_modules/,
             loader: 'babel-loader',
         },
 { 
        test: /\.css$/, 
        loader: "style-loader!css-loader" 
      },
{ 
        test: /\.png$/, 
        loader: "url-loader?limit=100000" 
      },
      { 
        test: /\.jpg$/, 
        loader: "file-loader" 
      },
      {
        test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=application/font-woff'
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=application/octet-stream'
      },
      {
        test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'file'
      },
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=image/svg+xml'
      }               
        ]
     },
    resolve: {
        modulesDirectories: ["node_modules"]
    }

 }

