nmap <silent> <leader><bar> :call ToggleIndentGuidesTabs()<cr>
nmap <silent> <leader><bslash> :call ToggleIndentGuidesSpaces()<cr>

function! ToggleIndentGuidesTabs()
    if exists('b:iguides_tabs')
	setlocal nolist
	let &l:listchars = b:iguides_tabs
	unlet b:iguides_tabs
    else
	let b:iguides_tabs = &l:listchars
	setlocal listchars=tab:┆\ "protect the space
	setlocal list
    endif
endfunction

function! ToggleIndentGuidesSpaces()
    if exists('b:iguides_spaces')
	call matchdelete(b:iguides_spaces)
	unlet b:iguides_spaces
    else
	let pos = range(1, &l:textwidth, &l:shiftwidth)
	call map(pos, '"\\%" . v:val . "v"')
	let pat = '\%(\_^\s*\)\@<=\%(' . join(pos, '\|') . '\)\s'
	let b:iguides_spaces = matchadd('CursorLine', pat)
    endif
endfunction

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab
" display indentation guides
"set list listchars=tab:❘-,trail:·,extends:»,precedes:«,nbsp:×
"set list listchars=tab:»·,trail:·,extends:#

