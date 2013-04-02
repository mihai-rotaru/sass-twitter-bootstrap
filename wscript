# vim:filetype=python
top = '.'
out = 'bootstrap'

BOOTSTRAP_SCSS              = 'lib/bootstrap.scss'
BOOTSTRAP                   = 'css/bootstrap.css'

BOOTSTRAP_RESPONSIVE_SCSS   = 'lib/responsive.scss'
BOOTSTRAP_RESPONSIVE        = 'css/bootstrap-responsive.css'

def configure(ctx):
    ctx.find_program( 'uglifyjs' )
    ctx.find_program( 'sass' )

def ext_prepend(fname, prefix):
    return fname[:fname.rfind('.')+1] + 'min' + fname[fname.rfind('.'):]

def build(bld):
    sass    = 'sass --unix-newlines ${SRC} ${TGT}'
    sass_c  = 'sass --unix-newlines --style compressed ${SRC} ${TGT}'
    bld( rule = sass,   source = BOOTSTRAP_SCSS, target = BOOTSTRAP )
    bld( rule = sass,   source = BOOTSTRAP_RESPONSIVE_SCSS, target = BOOTSTRAP_RESPONSIVE )
    bld( rule = sass_c, source = BOOTSTRAP_SCSS, target = ext_prepend(BOOTSTRAP,'min') )
    bld( rule = sass_c, source = BOOTSTRAP_RESPONSIVE_SCSS, target = ext_prepend(BOOTSTRAP_RESPONSIVE, 'min') )
