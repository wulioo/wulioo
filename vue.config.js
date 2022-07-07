

module.exports = {
    // publicPath: '/',
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000/',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''   //需要rewrite重写的URL
                }
            },

        }
    }
}