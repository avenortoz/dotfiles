local null_ls_status_ok, null_ls = pcall(require, "null-ls")
if not null_ls_status_ok then
    return
end

-- https://github.com/jose-elias-alvarez/null-ls.nvim/tree/main/lua/null-ls/builtins/formatting
local formatting = null_ls.builtins.formatting
-- https://github.com/jose-elias-alvarez/null-ls.nvim/tree/main/lua/null-ls/builtins/diagnostics
local diagnostics = null_ls.builtins.diagnostics

null_ls.setup({
    debug = false,
    sources = {
        formatting.prettier.with({ extra_args = { "--no-semi", "--single-quote", "--jsx-single-quote" } }),
        formatting.black.with({ extra_args = { "--stdin-filename", "$FILENAME", "--quiet", "-" } }),
        formatting.stylua,
        diagnostics.flake8.with({extra_args = {"--ignore=E501"}}),
        diagnostics.cppcheck.with({ extra_args = { "--enable=warning,style,performance,portability", "--template=gcc",
            "$FILENAME" } }),
        diagnostics.golangci_lint.with({ extra_args = {"run", "--fix=false", "--fast", "--out-format=json", "$DIRNAME", "--path-prefix", "$ROOT"}}),
        -- formatting.clang_format,
    },
})
