var gulp = require('gulp'),
    gutil = require('gulp-util');

var plugins = require("gulp-load-plugins")({
    pattern: ['gulp-*', 'gulp.*'],
    replaceString: /\bgulp[\-.]/
});

var basePaths = {
    src: 'app/assets/',
    dest: 'public/',
    bower: 'public/components/'
};

var paths = {
    images: {
        src: basePaths.src + 'images/',
        dest: basePaths.dest + 'images/'
    },
    scripts: {
        src: basePaths.src + 'js/',
        dest: basePaths.dest + 'js/'
    },
    styles: {
        src: basePaths.src + 'scss/',
        dest: basePaths.dest + 'css/'
    }
};

var appFiles = {
    images: paths.images.src + '**/*',
    styles: paths.styles.src + '**/*.scss',
    scripts: paths.scripts.src + '**/*.js'
};

var onError = function (err) {
    gutil.beep();
    gutil.log(gutil.colors.white(err.plugin), gutil.colors.red(err.message));
    plugins.notify.onError("<%= err.message %>");
    this.emit('end');
};

gulp.task('css', function () {
    gulp.src(appFiles.styles)
        .pipe(plugins.plumber({errorHandler: onError}))
        .pipe(plugins.sass({ includePaths: [basePaths.bower, basePaths.bower + '/foundation/scss/'] }))
        .pipe(plugins.importCss())
        //.pipe(plugins.minifyCss({ keepSpecialComments: '0' }))
        .pipe(plugins.autoprefixer('Explorer >= 9', 'Android >= 2', 'iOS >= 5', '> 1%'))
        //.pipe(plugins.size())
        .pipe(gulp.dest(paths.styles.dest))
        .pipe(plugins.livereload())
        .pipe(plugins.notify('CSS updated.'));
});

gulp.task('js', function() {
    gulp.src(paths.scripts.src + '/app.js')
        .pipe(plugins.plumber({errorHandler: onError}))
        .pipe(plugins.include())
        //.pipe(plugins.uglify())
        //.pipe(plugins.size())
        .pipe(gulp.dest(paths.scripts.dest))
        .pipe(plugins.notify('JavaScript updated.'));
});

gulp.task('watch', function () {
    gulp.watch(appFiles.styles, ['css']);
    gulp.watch(appFiles.scripts, ['js']);
});

gulp.task('default', ['css', 'js', 'watch']);
