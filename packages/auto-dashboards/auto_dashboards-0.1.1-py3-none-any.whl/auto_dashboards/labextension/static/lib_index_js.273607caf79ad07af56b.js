"use strict";
(self["webpackChunk_orbrx_auto_dashboards"] = self["webpackChunk_orbrx_auto_dashboards"] || []).push([["lib_index_js"],{

/***/ "./lib/button.js":
/*!***********************!*\
  !*** ./lib/button.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   StreamlitButtonExtension: () => (/* binding */ StreamlitButtonExtension)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");
/*
 * Copyright 2017-2023 Elyra Authors
 * Copyright 2025 Orange Bricks
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



class StreamlitButtonExtension {
    constructor(commands) {
        this.commands = commands;
    }
    createNew(widget) {
        let button;
        const filePath = widget.context.path;
        if (filePath.endsWith('.py')) {
            button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.CommandToolbarButton({
                commands: this.commands,
                id: _utils__WEBPACK_IMPORTED_MODULE_2__.CommandIDs.openFromEditor,
                label: '',
                args: { file: widget.context.path }
            });
        }
        else if (filePath.endsWith('.ipynb')) {
            button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.CommandToolbarButton({
                commands: this.commands,
                id: _utils__WEBPACK_IMPORTED_MODULE_2__.CommandIDs.translate,
                label: '',
                args: { file: widget.context.path }
            });
        }
        else {
        }
        if (button) {
            widget.toolbar.insertItem(99, 'streamlit', button);
        }
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            button === null || button === void 0 ? void 0 : button.dispose();
        });
    }
}


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
/*
 * Copyright 2017-2023 Elyra Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'streamlit', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data;
    try {
        data = await response.json();
    }
    catch (error) {
        console.log('Not a JSON response body.', response);
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data || response;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   checkCookie: () => (/* binding */ checkCookie),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   syncXsrfCookie: () => (/* binding */ syncXsrfCookie)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/fileeditor */ "webpack/sharing/consume/default/@jupyterlab/fileeditor");
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var path__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! path */ "./node_modules/path-browserify/index.js");
/* harmony import */ var path__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(path__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _button__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./button */ "./lib/button.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");
/*
 * Copyright 2017-2023 Elyra Authors
 * Copyright 2025 Orange Bricks
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */









const NAMESPACE = '@orbrx/auto-dashboards';
const serverErrorMessage = 'There was an issue with the auto_dashboards server extension.';
const syncXsrfCookie = () => {
    const xsrf = (0,_utils__WEBPACK_IMPORTED_MODULE_6__.getCookie)('_xsrf');
    const jupyterlab_xsrf = (0,_utils__WEBPACK_IMPORTED_MODULE_6__.getCookie)('jupyterlab_xsrf');
    // Initialize or update jupyterlab_xsrf to duplicate _xsrf
    if (xsrf && (!jupyterlab_xsrf || xsrf !== jupyterlab_xsrf)) {
        document.cookie = 'jupyterlab_xsrf=' + xsrf;
    }
    // Restore _xsrf if deleted
    if (jupyterlab_xsrf && !xsrf) {
        document.cookie = '_xsrf=' + jupyterlab_xsrf;
    }
};
const checkCookie = (function () {
    syncXsrfCookie();
    let previousCookie = document.cookie;
    return () => {
        const currentCookie = document.cookie;
        if (currentCookie !== previousCookie) {
            syncXsrfCookie();
            previousCookie = currentCookie;
        }
    };
})();
const getStreamlitApp = async (file) => {
    try {
        const data = await (0,_handler__WEBPACK_IMPORTED_MODULE_7__.requestAPI)('app', {
            method: 'POST',
            body: JSON.stringify({ file })
        });
        return data.url;
    }
    catch (reason) {
        console.error(`${serverErrorMessage}\n${reason}`);
        return undefined;
    }
};
const stopStreamlitApp = async (file) => {
    try {
        await (0,_handler__WEBPACK_IMPORTED_MODULE_7__.requestAPI)('app', {
            method: 'DELETE',
            body: JSON.stringify({ file })
        });
    }
    catch (reason) {
        console.error(`${serverErrorMessage}\n${reason}`);
    }
};
const translateNotebook = async (file, id) => {
    try {
        console.log('translateNotebook called with file:', file);
        const data = await (0,_handler__WEBPACK_IMPORTED_MODULE_7__.requestAPI)('translate', {
            method: 'POST',
            body: JSON.stringify({ file })
        });
        console.log('translateNotebook response:', data);
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.update({
            id,
            message: 'Dashboard is ready',
            type: 'success',
            autoClose: 2000
        });
        return data.url;
    }
    catch (reason) {
        console.error(`${serverErrorMessage}\n${reason}`);
        if (reason instanceof Error) {
            (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)('Error translating notebook', reason);
        }
        else {
            (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)('Error translating notebook', new Error(String(reason)));
        }
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.update({
            id,
            message: `Error translating notebook: ${reason}`,
            type: 'error',
            autoClose: false
        });
        return undefined;
    }
};
/**
 * Initialization data for the auto-dashboardsextension extension.
 */
const plugin = {
    id: NAMESPACE,
    autoStart: true,
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__.IEditorTracker, _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__.IFileBrowserFactory],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    activate: (app, editorTracker, factory, restorer) => {
        console.log('JupyterLab extension auto-dashboards is activated!');
        (0,_handler__WEBPACK_IMPORTED_MODULE_7__.requestAPI)('app')
            .then(data => {
            console.log('auto_dashboards server extension successfully started');
        })
            .catch(reason => {
            console.error(`${serverErrorMessage}\n${reason}`);
        });
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: NAMESPACE
        });
        // Handle state restoration
        if (restorer) {
            void restorer.restore(tracker, {
                command: _utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.open,
                args: widget => ({
                    file: widget.id.split(':')[1]
                }),
                name: widget => widget.id
            });
        }
        app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.translate, {
            label: 'Translate Notebook to Streamlit',
            icon: _utils__WEBPACK_IMPORTED_MODULE_6__.streamlitIcon,
            execute: async () => {
                console.log('Translate command executed');
                const widget = app.shell.currentWidget;
                if (!widget) {
                    console.log('No active widget found');
                    return;
                }
                let filePath;
                // Use context.path if available for notebook panels, otherwise fallback to widget.id splitting
                if (widget.context && widget.context.path) {
                    filePath = widget.context.path;
                }
                else {
                    filePath = widget.id.split(':')[1];
                }
                if (!(0,_utils__WEBPACK_IMPORTED_MODULE_6__.isNotebook)(filePath)) {
                    console.log('No notebook found');
                    return;
                }
                console.log('Calling translateNotebook with path:', filePath);
                const id = _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.emit('Creating dashboard...', 'in-progress', {
                    autoClose: false
                });
                const url = await translateNotebook(filePath, id);
                console.log('translateNotebook returned URL:', url);
                if (url) {
                    const translatedFilePath = filePath.replace(/\.ipynb$/, '.py');
                    await app.commands.execute(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.open, { file: translatedFilePath });
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.dismiss(id);
                }
            },
        });
        app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.open, {
            label: 'Streamlit',
            icon: _utils__WEBPACK_IMPORTED_MODULE_6__.streamlitIcon,
            execute: async (args) => {
                const widgetId = `${NAMESPACE}:${args.file}`;
                const openWidget = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__.find)(app.shell.widgets('main'), (widget, index) => {
                    return widget.id === widgetId;
                });
                if (openWidget) {
                    app.shell.activateById(widgetId);
                    return;
                }
                const urlPromise = getStreamlitApp(args.file);
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IFrame({
                    sandbox: [
                        'allow-same-origin',
                        'allow-scripts',
                        'allow-popups',
                        'allow-forms'
                    ]
                });
                const main = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content: widget });
                main.title.label = path__WEBPACK_IMPORTED_MODULE_5___default().basename(args.file);
                main.title.icon = _utils__WEBPACK_IMPORTED_MODULE_6__.streamlitIcon;
                main.title.caption = widget.title.label;
                main.id = widgetId;
                main.disposed.connect(() => {
                    stopStreamlitApp(args.file);
                });
                await tracker.add(main);
                app.shell.add(main, 'main', { mode: 'split-right' });
                // Set iframe url last to not block widget creation on webapp startup
                const url = await urlPromise;
                // When iframe src=undefined the lab instance is shown instead
                // In this case we want to close the widget rather than set the url
                if (url === undefined) {
                    main.dispose();
                    void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                        title: 'Streamlit application failed to start',
                        body: 'Check the logs for more information.',
                        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                    });
                }
                else {
                    widget.url = url;
                }
            }
        });
        app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.openFromBrowser, {
            label: 'Run in Streamlit',
            icon: _utils__WEBPACK_IMPORTED_MODULE_6__.streamlitIcon,
            isVisible: () => !!factory.tracker.currentWidget &&
                factory.tracker.currentWidget.selectedItems().next !== undefined,
            execute: async () => {
                const currentWidget = factory.tracker.currentWidget;
                if (!currentWidget) {
                    return;
                }
                const result = currentWidget.selectedItems().next();
                if (result.done || !result.value) {
                    return;
                }
                const item = result.value;
                await app.commands.execute(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.open, {
                    file: item.path
                });
            }
        });
        app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.openFromEditor, {
            execute: () => {
                const widget = editorTracker.currentWidget;
                if (!widget) {
                    return;
                }
                const path = widget.context.path;
                return app.commands.execute(_utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.open, { file: path });
            },
            icon: _utils__WEBPACK_IMPORTED_MODULE_6__.streamlitIcon,
            label: 'Run in Streamlit'
        });
        app.docRegistry.addWidgetExtension('Editor', new _button__WEBPACK_IMPORTED_MODULE_8__.StreamlitButtonExtension(app.commands));
        app.docRegistry.addWidgetExtension('Notebook', new _button__WEBPACK_IMPORTED_MODULE_8__.StreamlitButtonExtension(app.commands));
        app.contextMenu.addItem({
            selector: '[data-file-type="python"]',
            command: _utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.openFromBrowser,
            rank: 999
        });
        app.contextMenu.addItem({
            selector: '.jp-FileEditor',
            command: _utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.openFromEditor,
            rank: 999
        });
        app.contextMenu.addItem({
            selector: '.jp-Notebook',
            command: _utils__WEBPACK_IMPORTED_MODULE_6__.CommandIDs.translate,
            rank: 999
        });
        // Poll changes to cookies and prevent the deletion of _xsrf by Streamlit
        // _xsrf deletion issue: https://github.com/streamlit/streamlit/issues/2517
        window.setInterval(checkCookie, 100); // run every 100 ms
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CommandIDs: () => (/* binding */ CommandIDs),
/* harmony export */   getCookie: () => (/* binding */ getCookie),
/* harmony export */   isNotebook: () => (/* binding */ isNotebook),
/* harmony export */   streamlitIcon: () => (/* binding */ streamlitIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_streamlit_mark_color_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../style/streamlit-mark-color.svg */ "./style/streamlit-mark-color.svg");
/*
 * Copyright 2017-2023 Elyra Authors
 * Copyright 2025 Orange Bricks
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


const CommandIDs = {
    open: 'streamlit:open',
    openFromBrowser: 'streamlit:open-browser',
    openFromEditor: 'streamlit:open-file',
    translate: 'streamlit:translate'
};
const streamlitIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'streamlit:icon',
    svgstr: _style_streamlit_mark_color_svg__WEBPACK_IMPORTED_MODULE_1__
});
const getCookie = (key) => { var _a; return ((_a = document.cookie.match('(^|;)\\s*' + key + '\\s*=\\s*([^;]+)')) === null || _a === void 0 ? void 0 : _a.pop()) || ''; };
const isNotebook = (filePath) => {
    return filePath.endsWith('.ipynb');
};


/***/ }),

/***/ "./style/streamlit-mark-color.svg":
/*!****************************************!*\
  !*** ./style/streamlit-mark-color.svg ***!
  \****************************************/
/***/ ((module) => {

module.exports = "<svg width=\"301\" height=\"165\" viewBox=\"0 0 301 165\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">\n<path d=\"M150.731 101.547L98.1387 73.7471L6.84674 25.4969C6.7634 25.4136 6.59674 25.4136 6.51341 25.4136C3.18007 23.8303 -0.236608 27.1636 1.0134 30.497L47.5302 149.139L47.5385 149.164C47.5885 149.281 47.6302 149.397 47.6802 149.514C49.5885 153.939 53.7552 156.672 58.2886 157.747C58.6719 157.831 58.9461 157.906 59.4064 157.998C59.8645 158.1 60.5052 158.239 61.0552 158.281C61.1469 158.289 61.2302 158.289 61.3219 158.297H61.3886C61.4552 158.306 61.5219 158.306 61.5886 158.314H61.6802C61.7386 158.322 61.8052 158.322 61.8636 158.322H61.9719C62.0386 158.331 62.1052 158.331 62.1719 158.331V158.331C121.084 164.754 180.519 164.754 239.431 158.331V158.331C240.139 158.331 240.831 158.297 241.497 158.231C241.714 158.206 241.922 158.181 242.131 158.156C242.156 158.147 242.189 158.147 242.214 158.139C242.356 158.122 242.497 158.097 242.639 158.072C242.847 158.047 243.056 158.006 243.264 157.964C243.681 157.872 243.87 157.806 244.436 157.611C245.001 157.417 245.94 157.077 246.527 156.794C247.115 156.511 247.522 156.239 248.014 155.931C248.622 155.547 249.201 155.155 249.788 154.715C250.041 154.521 250.214 154.397 250.397 154.222L250.297 154.164L150.731 101.547Z\" fill=\"#FF4B4B\"/>\n<path d=\"M294.766 25.4981H294.683L203.357 73.7483L254.124 149.357L300.524 30.4981V30.3315C301.691 26.8314 298.108 23.6648 294.766 25.4981\" fill=\"#7D353B\"/>\n<path d=\"M155.598 2.55572C153.264 -0.852624 148.181 -0.852624 145.931 2.55572L98.1389 73.7477L150.731 101.548L250.398 154.222C251.024 153.609 251.526 153.012 252.056 152.381C252.806 151.456 253.506 150.465 254.123 149.356L203.356 73.7477L155.598 2.55572Z\" fill=\"#BD4043\"/>\n</svg>\n";

/***/ })

}]);
//# sourceMappingURL=lib_index_js.273607caf79ad07af56b.js.map