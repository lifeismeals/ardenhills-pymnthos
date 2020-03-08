"Don't put anything in your .vimrc you don't understand!


syntax enable 

autocmd FileType make setlocal noexpandtab
autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab|set softtabstop=4
autocmd FileType go set tabstop=4|set shiftwidth=4|set expandtab|set softtabstop=4
autocmd FileType ruby set tabstop=2|set shiftwidth=2|set expandtab|set softtabstop=2
autocmd FileType perl set tabstop=8|set shiftwidth=8|set expandtab|set softtabstop=8
autocmd FileType * set tabstop=4|set shiftwidth=4|set noexpandtab|set softtabstop=4

colorscheme evening 
set number
set showcmd
set cursorline
filetype indent on
set showmatch
set hlsearch


