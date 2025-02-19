"use strict";
(self["webpackChunkjupyterlab_autodocstring"] = self["webpackChunkjupyterlab_autodocstring"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);


/**
 * The command IDs used by the plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.generateDocstring = 'autodocstring:generate';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the jupyterlab_autodocstring extension.
 */
const plugin = {
    id: 'jupyterlab_autodocstring:plugin',
    description: 'Automatically insert docstring template after writing function header.',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, tracker, palette) => {
        console.log('JupyterLab extension jupyterlab_autodocstring is activated!');
        // Register our command
        app.commands.addCommand(CommandIDs.generateDocstring, {
            label: 'Generate Docstring',
            execute: () => {
                console.log('Executing command:', CommandIDs.generateDocstring);
                // Get the current active notebook and editor
                const current = tracker.currentWidget;
                if (!current) {
                    return;
                }
                const cell = current.content.activeCell;
                if (!cell) {
                    return;
                }
                const editor = cell.editor;
                if (!editor) {
                    return;
                }
                generateDocstring(editor);
            }
        });
        // ✅ Add the command to the command palette
        palette.addItem({
            command: CommandIDs.generateDocstring,
            category: 'Docstring Tools'
        });
        // ✅ Manually Listen for 'Cmd + Shift + D' inside Jupyter Notebook Cells
        document.addEventListener("keydown", (event) => {
            // ✅ Intercept 'Tab' key only if in a valid function docstring context
            if (event.code === "Tab") {
                const activeCell = tracker.activeCell;
                if (!activeCell)
                    return;
                const editor = activeCell.editor;
                if (!editor)
                    return;
                const cursor = editor.getCursorPosition();
                const lines = editor.model.sharedModel.getSource().split("\n");
                // ✅ Check if current line is a triple-quote (`"""`)
                const currentLine = lines[cursor.line].trim();
                if (currentLine !== `""""""`)
                    return; // Normal tab if not triple quotes
                // ✅ Look for the closest function definition above
                let funcLineIndex = -1;
                for (let i = cursor.line - 1; i >= 0; i--) {
                    if (/^\s*def\s+\w+\s*\(.*\)\s*:/.test(lines[i])) {
                        funcLineIndex = i;
                        break;
                    }
                }
                if (funcLineIndex === -1)
                    return; // Normal tab if no function found
                console.log("🔍 Function detected! Replacing triple-quotes with docstring template.");
                event.preventDefault();
                event.stopPropagation();
                app.commands.execute(CommandIDs.generateDocstring);
            }
        });
    }
};
/**
 * Generates a docstring template in the given editor.
 */
function generateDocstring(editor) {
    var _a;
    const cursor = editor.getCursorPosition();
    const line = editor.getLine(cursor.line) || '';
    // Check if the current line is exactly sextuple quotes (allowing for spaces)
    const match = line.match(/^(\s*)""""""\s*$/);
    if (!match) {
        return;
    }
    const indentation = match[1]; // Capture the leading spaces (indentation)
    // Get all the text from the start of the cell to the current line.
    const cellText = editor.model.sharedModel.getSource();
    const lines = cellText.split('\n');
    // Find the function definition before the current line.
    let funcLineIndex = -1;
    for (let i = cursor.line - 1; i >= 0; i--) {
        if (/^\s*def\s+\w+\s*\(.*\)\s*:/.test(lines[i])) {
            funcLineIndex = i;
            break;
        }
    }
    if (funcLineIndex === -1) {
        console.warn('No function signature found above the docstring.');
        return;
    }
    const funcLine = lines[funcLineIndex];
    const paramMatch = funcLine.match(/\((.*)\)/);
    let params = [];
    if (paramMatch && paramMatch[1].trim()) {
        // Split parameters by comma and trim them.
        params = paramMatch[1].split(',').map((param) => param.trim().split('=')[0]);
    }
    // Create a docstring template with the correct indentation
    let docstringTemplate = `${indentation}"""\n${indentation}{Summary}\n\n`;
    if (params.length) {
        docstringTemplate += `${indentation}Args:\n`;
        params.forEach(param => {
            docstringTemplate += `${indentation}    ${param}: \n`;
        });
        docstringTemplate += `\n`;
    }
    docstringTemplate += `${indentation}Returns:\n${indentation}    {return}\n${indentation}"""`;
    // Replace the current line (six quotes) with the docstring template.
    lines[cursor.line] = docstringTemplate;
    // Update the editor content
    editor.model.sharedModel.setSource(lines.join("\n"));
    // ✅ Move cursor to the end of the inserted docstring
    const newCursorLine = cursor.line + docstringTemplate.split("\n").length - 1;
    const newCursorColumn = ((_a = docstringTemplate.split("\n").pop()) === null || _a === void 0 ? void 0 : _a.length) || 0;
    editor.setCursorPosition({ line: newCursorLine, column: newCursorColumn });
    // console.log("✅ Docstring inserted with proper indentation!");
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.f827baad76e4d32ab7af.js.map