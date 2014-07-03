module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({

        concat: {
            // 2. Configuration for concatinating files goes here.
                dist: {
                    src: [
                        'static/js/jquery-1.11.1.min.js', // a JS in the  folder
                          // This specific file
                    ],
                    dest: 'static/js/build/production.js',
                }
        }


        // watch: {
        //     html:{
        //         files: '/templates/doit/*.html',
        //         options:{
        //             livereload: 8000,
        //         },
        //     },

        //     // scripts: {
        //     //     files: ['static/css/*.css', 'templates/doit/*.html'],
        //     // } 
        // }





    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', [ 'concat']);

};
