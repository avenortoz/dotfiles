local options = {
    backup = false, -- creates a backup file
    clipboard = "unnamedplus", -- allows neovim to access the system clipboard
    cmdheight = 2, -- more space in the neovim command line for displaying messages
    completeopt = { "menuone", "noselect" }, -- mostly just for cmp
    conceallevel = 0, -- so that `` is visible in markdown files
    fileencoding = "utf-8", -- the encoding written to a file
    hlsearch = true, -- highlight all matches on previous search pattern
    ignorecase = true, -- ignore case in search patterns
    mouse = "a", -- allow the mouse to be used in neovim
    pumheight = 10, -- pop up menu height
    showmode = false, -- we don't need to see things like -- INSERT -- anymore
    showtabline = 4, -- always show tabs
    smartcase = true, -- smart case
    smartindent = true, -- make indenting smarter again
    splitbelow = true, -- force all horizontal splits to go below current window
    splitright = true, -- force all vertical splits to go to the right of current window
    swapfile = false, -- creates a swapfile
    termguicolors = true, -- set term gui colors (most terminals support this)
    timeoutlen = 500, -- time to wait for a mapped sequence to complete (in milliseconds)
    undofile = true, -- enable persistent undo
    updatetime = 300, -- faster completion (4000ms default)
    writebackup = false, -- if a file is being edited by another program (or was written to file while editing with another program), it is not allowed to be edited
    expandtab = true, -- convert tabs to spaces
    shiftwidth = 4, -- the number of spaces inserted for each indentation
    tabstop = 4, -- insert 2 spaces for a tab
    cursorline = true, -- highlight the current line
    number = true, -- set numbered lines
    relativenumber = true, -- set relative numbered lines
    numberwidth = 4, -- set number column width to 2 {default 4}
    signcolumn = "yes", -- always show the sign column, otherwise it would shift the text each time
    wrap = false, -- display lines as one long line
    scrolloff = 8, -- is one of my fav
    sidescrolloff = 8,
    guifont = "monospace:h17", -- the font used in graphical neovim applications
}

vim.opt.shortmess:append "c"

for k, v in pairs(options) do
    vim.opt[k] = v
end

vim.cmd "set whichwrap+=<,>,[,],h,l"
vim.cmd [[set iskeyword+=-]]
vim.cmd [[set formatoptions-=cro]] -- TODO: this doesn't seem to work
vim.cmd("set langmap=йq,цw,уe,кr,еt,нy,гu,шi,щo,зp,фa,іs,вd,аf,пg,рh,оj,лk,дl,яz,чx,сc,мv,иb,тn,ьm")
-- For tmux to not swap line after ESC
-- vim.keys.insert_mode["<A-j>"] = false
-- vim.keys.insert_mode["<A-k>"] = false
-- vim.keys.normal_mode["<A-j>"] = false
-- vim.keys.normal_mode["<A-k>"] = false
-- vim.keys.visual_block_mode["<A-j>"] = false
-- vim.keys.visual_block_mode["<A-k>"] = false
-- vim.keys.visual_block_mode["J"] = false
-- vim.keys.visual_block_mode["K"] = false

-- vim.cmd "au ColorScheme * hi Normal ctermbg=none guibg=none"
-- vim.cmd "au ColorScheme * hi SignColumn ctermbg=none guibg=none"
-- vim.cmd "au ColorScheme * hi NormalNC ctermbg=none guibg=none"
-- vim.cmd "au ColorScheme * hi MsgArea ctermbg=none guibg=none"
-- vim.cmd "au ColorScheme * hi TelescopeBorder ctermbg=none guibg=none"
-- vim.cmd "au ColorScheme * hi NvimTreeNormal ctermbg=none guibg=none"
-- vim.cmd "let &fcs='eob: '"
