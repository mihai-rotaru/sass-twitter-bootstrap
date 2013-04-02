# vim:filetype=python
top = '.'
out = 'bootstrap'

BOOTSTRAP_SCSS              = 'lib/bootstrap.scss'
BOOTSTRAP                   = 'css/bootstrap.css'

BOOTSTRAP_RESPONSIVE_SCSS   = 'lib/responsive.scss'
BOOTSTRAP_RESPONSIVE        = 'css/bootstrap-responsive.css'

BOOTSTRAP_JAVASCRIPTS       = 'js/bootstrap.js'

def configure(ctx):
    ctx.find_program( 'uglifyjs' )
    ctx.find_program( 'sass' )

def ext_prepend(fname, prefix):
    return fname[:fname.rfind('.')+1] + 'min' + fname[fname.rfind('.'):]

def build(bld):
    # compile scss files
    sass    = 'sass --unix-newlines ${SRC} ${TGT}'
    bld( rule = sass,   source = BOOTSTRAP_SCSS, target = BOOTSTRAP )
    bld( rule = sass,   source = BOOTSTRAP_RESPONSIVE_SCSS, target = BOOTSTRAP_RESPONSIVE )

    # compile scss files into minified css files
    sass_c  = 'sass --unix-newlines --style compressed ${SRC} ${TGT}'
    bld( rule = sass_c, source = BOOTSTRAP_SCSS, target = ext_prepend(BOOTSTRAP,'min') )
    bld( rule = sass_c, source = BOOTSTRAP_RESPONSIVE_SCSS, target = ext_prepend(BOOTSTRAP_RESPONSIVE, 'min') )

    # concatenate javascripts
    def read_entirely( file ):
        with open( file, 'r' ) as handle:
            return handle.read()
    def concatenate_files_fun( task ):
        files = []
        for file in task.inputs:
            files.append( file.abspath() )
        result = '\n'.join( read_entirely( file ) for file in files )
        with open( task.outputs[0].abspath(), 'w') as handle:
            handle.write( result )

    javascripts = bld.path.ant_glob( ['js/*.js'], exc=['build'] ) 
    bld( rule = concatenate_files_fun, source = javascripts, target = BOOTSTRAP_JAVASCRIPTS )
