"use strict";

var config = {
    server: {
        baseDir: './dist'
    },
    notify: false
};

const path = {
    dist: {
        html: 'dist/',
        js: 'dist/js/',
        jsmain: 'dist/js',
        css: 'dist/css/',
        img: 'dist/img/',
        fonts: 'dist/fonts/'
    },
    src: {
        html: 'src/*.html',
        js: 'src/js/*.js',
        jsmain: 'src/js/main.js',
        scss: 'src/css/main.scss',
        css: 'src/css/*.css',
        img: 'src/img/**/*.*',
        fonts: 'src/fonts/**/*.*'
    },
    watch: {
        html: 'src/*.html',
        htmlTemplate: 'src/template/*.html',
        js: 'src/js/*.js',
        jsmain: 'src/js/main.js',
        scss: 'src/css/**/*.scss',
        css: 'src/css/styles/*.scss',
        img: 'src/img/**/*.*',
        fonts: 'src/fonts/**/*.*'
    },
    clean: './dist/'
};

const gulp = require('gulp')
const browserSync = require('browser-sync').create();
const plumber = require('gulp-plumber');
const rigger = require('gulp-rigger');
const sourcemaps = require('gulp-sourcemaps');
const sass = require('gulp-sass');
const autoprefixer = require('autoprefixer');
const cleanCSS = require('gulp-clean-css');
const uglify = require('gulp-uglify');
const cache = require('gulp-cache');
const imagemin = require('gulp-imagemin');
const jpegrecompress = require('imagemin-jpeg-recompress');
const pngquant = require('imagemin-pngquant');
const del = require('del');
const postcss = require('gulp-postcss');

/* Tasks */

gulp.task('browserSync', (done) => {
    browserSync.init(config);
    done();
});

gulp.task('html:build', (done) => {
    gulp.src(path.src.html)
        .pipe(plumber())
        .pipe(rigger())
        .pipe(gulp.dest(path.dist.html))
        .pipe(browserSync.reload({stream: true}))
    done();
});

gulp.task('scss:build', (done) => {
    gulp.src(path.src.scss)
        .pipe(plumber())
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: 'compact'
        }).on('error', sass.logError))
        .pipe(postcss([autoprefixer({browsers: ['last 1 version']})]))
        .pipe(cleanCSS({
            level: 2
        }, (details) => {
            console.log(`${details.name}: ${details.stats.originalSize}`);
            console.log(`${details.name}: ${details.stats.minifiedSize}`);
        }))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(path.dist.css))
        .pipe(browserSync.reload({stream: true}));
    done();
})

gulp.task('css:build', (done) => {
    gulp.src(path.src.css)
        .pipe(gulp.dest(path.dist.css));
    done();
});

gulp.task('jsmain:build', (done) => {
    gulp.src(path.src.jsmain)
        .pipe(plumber())
        .pipe(rigger())
        .pipe(sourcemaps.init())
        .pipe(uglify())
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(path.dist.jsmain))
        .pipe(browserSync.reload({ stream: true }));
    done();
})

gulp.task('js:build', function (done) {
    gulp.src([path.src.js, '!app/js/main.js'])
        .pipe(gulp.dest(path.dist.js));
    done();
});


gulp.task('fonts:build', (done) => {
    gulp.src(path.src.fonts)
        .pipe(gulp.dest(path.dist.fonts));
    done();
});

gulp.task('image:build', (done) => {
    gulp.src(path.src.img)
        .pipe(cache(imagemin([
            imagemin.gifsicle({ interlaced: true }),
            jpegrecompress({
                progressive: true,
                max: 90,
                min: 80
            }),
            pngquant(),
            imagemin.svgo({ plugins: [{ removeViewBox: false }] })
        ])))
        .pipe(gulp.dest(path.dist.img));
    done();
})

gulp.task('clean:build', (done) => {
    del.sync(path.clean);
    done();
});

gulp.task('cache:clear', (done) => {
    cache.clearAll();
    done();
});

gulp.task('build', gulp.series('clean:build', 'html:build', 'scss:build', 'css:build', 'js:build', 'jsmain:build', 'fonts:build', 'image:build',(done) => {
    done();
}));

gulp.task('watch', () => {
    gulp.watch(path.watch.html, gulp.series('html:build'));
    gulp.watch(path.watch.htmlTemplate, gulp.series('html:build'));
    gulp.watch(path.watch.css, gulp.series('css:build'));
    gulp.watch(path.watch.scss, gulp.series('scss:build'));
    gulp.watch(path.watch.js, gulp.series('js:build'));
    gulp.watch(path.watch.img, gulp.series('image:build'));
    gulp.watch(path.watch.fonts, gulp.series('fonts:build'));
    gulp.watch(path.watch.jsmain, gulp.series('jsmain:build'));
});

gulp.task('default', gulp.series('clean:build', 'build', gulp.parallel('browserSync', 'watch')));