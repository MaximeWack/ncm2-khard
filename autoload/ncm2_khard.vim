if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:ncm2_khard#proc = yarp#py3({
    \ 'module': 'ncm2_khard',
    \ 'on_load': { -> ncm2#set_ready(g:ncm2_khard#source)}
    \ })

let g:ncm2_khard#source = extend(get(g:, 'ncm2_khard#source', {}), {
            \ 'name': 'khard',
            \ 'ready': 0,
            \ 'priority': 5,
            \ 'mark': 'email',
            \ 'scope': ['mail'],
            \ 'complete_pattern': ['^To: .*', '^Cc: .*', '^Bcc: .*'],
            \ 'complete_length': -1,
            \ 'on_complete': 'ncm2_khard#on_complete',
            \ 'on_warmup': 'ncm2_khard#on_warmup',
            \ }, 'keep')

func! ncm2_khard#init()
    call ncm2#register_source(g:ncm2_khard#source)
endfunc

func! ncm2_khard#on_warmup(ctx)
    call g:ncm2_khard#proc.try_notify('on_warmup', a:ctx)
endfunc

func! ncm2_khard#on_complete(ctx)
    call g:ncm2_khard#proc.try_notify('on_complete', a:ctx)
endfunc

func! ncm2_khard#on_event(event)
    call g:ncm2_khard#proc.try_notify('on_event', a:event, bufnr('%'))
  endfunc
