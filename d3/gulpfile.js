var gulp = require('gulp');
var watch = require('gulp-watch');
var sass = require('gulp-sass');
var prefix = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var lr = require('tiny-lr');
var server = lr()

var gzip_options = {
	threshold: '1kb',
	gzipOptions: {
		level: 9
	}
};

function errorHandler (e) {
	console.log(error.toString());
	this.emit('end');
}

/* Compile sass */
gulp.task('sass', function() {

	return gulp.src(['assets/_scss/*.scss', 'assets/_scss/*.sass'])
		.pipe(sass()).on('e', errorHandler)
		.pipe(prefix(['last 10 versions', '> 1%', 'ie 8', 'ie 7'], { cascade: true }))
		.pipe(gulp.dest('assets/css/css'))
		.pipe(rename({suffix: '.min'}))
		.pipe(minifycss())
		.pipe(gulp.dest('assets/css'))
		.pipe(gzip(gzip_options))
		.pipe(gulp.dest('assets/css/css'))
		.pipe(livereload(server));
});


/* Watch Changes */
gulp.task('watch', function() {
	livereload.listen(35729, function(err) {
		if (err) return gutil.log(err);
	});
	/* Run 'sass' task on any sass files */
	gulp.watch(['assets/_scss/**'], ['sass']);
	/* Live-reload when any templates or assets change */
	gulp.watch(['assets/_scss/**', 'assets/js/**', 'templates/**']).on('change', livereload.changed);
});

gulp.task('default', ['sass', 'watch']);