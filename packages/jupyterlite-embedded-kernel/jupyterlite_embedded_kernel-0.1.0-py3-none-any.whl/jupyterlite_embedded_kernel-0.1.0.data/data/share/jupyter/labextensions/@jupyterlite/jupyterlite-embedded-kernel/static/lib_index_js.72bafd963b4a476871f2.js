"use strict";
(self["webpackChunkjupyterlite_embedded_kernel"] = self["webpackChunkjupyterlite_embedded_kernel"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlite/kernel */ "webpack/sharing/consume/default/@jupyterlite/kernel");
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _kernel__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./kernel */ "./lib/kernel.js");


/**
 * Plugin configuration for the enhanced kernel
 */
const enhancedKernel = {
    id: 'enhanced-kernel-plugin',
    autoStart: true,
    requires: [_jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__.IKernelSpecs],
    activate: (app, kernelspecs) => {
        const activeKernels = new Map();
        app.router.post('/api/kernels/(.*)/interrupt', async (req, kernelId) => {
            const kernel = activeKernels.get(kernelId);
            if (kernel) {
                try {
                    await kernel.interrupt();
                    return new Response(null, { status: 204 });
                }
                catch (error) {
                    console.error('Failed to interrupt kernel:', error);
                    return new Response('Failed to interrupt kernel', { status: 500 });
                }
            }
            return new Response('Kernel not found', { status: 404 });
        });
        kernelspecs.register({
            spec: {
                name: 'enhanced',
                display_name: 'Enhanced Kernel',
                language: 'python',
                argv: [],
                resources: {
                    'logo-32x32': '',
                    'logo-64x64': '',
                },
            },
            create: async (options) => {
                const kernel = new _kernel__WEBPACK_IMPORTED_MODULE_1__.EchoKernel(options);
                activeKernels.set(kernel.id, kernel);
                async function connectSerialPort() {
                    var _a, _b;
                    try {
                        const port = await navigator.serial.requestPort();
                        await port.open({ baudRate: 115200 });
                        //
                        await port.setSignals({ dataTerminalReady: false });
                        await new Promise((resolve) => setTimeout(resolve, 200));
                        await port.setSignals({ dataTerminalReady: true });
                        //
                        // await port.open({ baudRate: 115200 });
                        const reader = (_a = port.readable) === null || _a === void 0 ? void 0 : _a.getReader();
                        const writer = (_b = port.writable) === null || _b === void 0 ? void 0 : _b.getWriter();
                        kernel.reader = reader;
                        kernel.writer = writer;
                        kernel.port = port;
                    }
                    catch (err) {
                        console.error('Serial Port Error:', err);
                    }
                }
                await connectSerialPort();
                console.log('Creating enhanced kernel instance');
                await kernel.ready;
                return kernel;
            },
        });
        console.log('Enhanced kernel plugin activated');
    },
};
const plugins = [enhancedKernel];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/kernel.js":
/*!***********************!*\
  !*** ./lib/kernel.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   EchoKernel: () => (/* binding */ EchoKernel)
/* harmony export */ });
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlite/kernel */ "webpack/sharing/consume/default/@jupyterlite/kernel");
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__);

/**
 * A kernel that echos content back.
 */
class EchoKernel extends _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_0__.BaseKernel {
    constructor() {
        super(...arguments);
        this.blocker = null;
        this.blockerResolve = null;
        this.first_run = true;
    }
    setBlocked(blocked) {
        if (blocked && !this.blocker) {
            this.blocker = new Promise((resolve) => {
                this.blockerResolve = resolve;
            });
        }
        else if (!blocked && this.blockerResolve) {
            this.blockerResolve();
            this.blocker = null;
            this.blockerResolve = null;
        }
    }
    async interrupt() {
        if (this.writer) {
            const ctrl_c = new Uint8Array([3]);
            const encoder = new TextEncoder();
            const new_line = encoder.encode('\r\n');
            await this.writer.write(ctrl_c);
            await this.writer.write(new_line);
        }
    }
    streamOutput(output) {
        this.stream({
            text: output,
            name: 'stdout',
        });
    }
    // /*
    //  * https://github.com/WICG/serial/issues/122
    //  */
    async readWithTimeout(timeoutMs = 500) {
        if (!this.reader) {
            return null;
        }
        const result = await this.reader.read();
        return result.value;
    }
    async read_loop() {
        let outputBuffer = ''; // Buffer to accumulate data
        const sendInterval = 500; // Interval in milliseconds to send data
        const sendData = () => {
            if (outputBuffer) {
                this.streamOutput(outputBuffer); // Send accumulated data
                console.log(outputBuffer);
                outputBuffer = ''; // Clear the buffer
            }
        };
        const intervalId = setInterval(sendData, sendInterval);
        try {
            while (this.reader) {
                const value = await this.readWithTimeout();
                if (!value) {
                    continue;
                }
                const data = new TextDecoder().decode(value);
                console.log('Current buffer before: ', outputBuffer);
                outputBuffer += data;
                console.log('Data: ', data);
                console.log('Current buffer after: ', outputBuffer);
                if (data.includes('>>>')) {
                    this.setBlocked(false);
                }
            }
        }
        finally {
            clearInterval(intervalId); // Stop the timer when exiting the loop
            sendData(); // Ensure remaining data is sent
        }
    }
    async waitForPrompt() {
        if (this.blocker) {
            await this.blocker;
        }
    }
    // async readUntilError() {
    //   try {
    //     while (this.reader) {
    //       const data  = await this.readWithTimeout();
    //       if (data){
    //         const value = new TextDecoder().decode(data);
    //         this.streamOutput(value)
    //       }
    //     }
    //   } catch (error) {
    //     console.error(error);
    //     return
    //   }
    // }
    async kernelInfoRequest() {
        const content = {
            implementation: 'embedded',
            implementation_version: '1.0.0',
            language_info: {
                codemirror_mode: {
                    name: 'python',
                    version: 3,
                },
                file_extension: '.py',
                mimetype: 'text/x-python',
                name: 'python',
                nbconvert_exporter: 'python',
                pygments_lexer: 'ipython3',
                version: '3.8',
            },
            protocol_version: '5.3',
            status: 'ok',
            banner: 'Echo Kernel with Serial Support',
            help_links: [
                {
                    text: 'Echo Kernel',
                    url: 'https://github.com/jupyterlite/echo-kernel',
                },
            ],
        };
        return content;
    }
    async executeRequest(content) {
        this.setBlocked(true);
        if (this.first_run) {
            this.read_loop();
            this.first_run = false;
        }
        const { code } = content;
        const encoder = new TextEncoder();
        // const ctrl_a = new Uint8Array([1])
        const ctrl_d = new Uint8Array([4]);
        const ctrl_e = new Uint8Array([5]);
        const new_line = encoder.encode('\r\n');
        console.log('2');
        if (this.writer) {
            await this.writer.write(ctrl_e);
            await this.writer.write(new_line);
            const data = encoder.encode(code);
            await this.writer.write(data);
            await this.writer.write(ctrl_d);
            await this.writer.write(new_line);
        }
        console.log('3');
        await this.waitForPrompt();
        console.log('4');
        return {
            status: 'ok',
            execution_count: this.executionCount,
            user_expressions: {},
        };
    }
    async completeRequest(content) {
        throw new Error('Not implemented');
    }
    async inspectRequest(content) {
        throw new Error('Not implemented');
    }
    async isCompleteRequest(content) {
        throw new Error('Not implemented');
    }
    async commInfoRequest(content) {
        throw new Error('Not implemented');
    }
    inputReply(content) { }
    async commOpen(msg) { }
    async commMsg(msg) { }
    async commClose(msg) { }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.72bafd963b4a476871f2.js.map