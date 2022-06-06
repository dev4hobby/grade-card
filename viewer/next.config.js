const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})
const webpack = require('webpack')
const compressionPlugin = require('compression-webpack-plugin')

module.exports = withBundleAnalyzer({
  compress: true,
  webpack(config) {
    // console.log(config)
    let prod = process.env.NODE_ENV === 'production'

    const plugins = [...config.plugins]
    if (prod) {
      plugins.push(new compressionPlugin())
    }
    return {
      ...config,
      mode: prod ? 'production' : 'development',
      devtool: prod ? 'hidden-source-map' : 'eval',
      plugins: plugins,
    }
  },
})
