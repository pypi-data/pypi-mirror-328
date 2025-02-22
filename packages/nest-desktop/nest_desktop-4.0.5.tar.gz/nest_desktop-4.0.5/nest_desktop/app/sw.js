/**
 * Copyright 2018 Google Inc. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// If the loader is already loaded, just stop.
if (!self.define) {
  let registry = {};

  // Used for `eval` and `importScripts` where we can't get script URL by other means.
  // In both cases, it's safe to use a global var because those functions are synchronous.
  let nextDefineUri;

  const singleRequire = (uri, parentUri) => {
    uri = new URL(uri + ".js", parentUri).href;
    return registry[uri] || (
      
        new Promise(resolve => {
          if ("document" in self) {
            const script = document.createElement("script");
            script.src = uri;
            script.onload = resolve;
            document.head.appendChild(script);
          } else {
            nextDefineUri = uri;
            importScripts(uri);
            resolve();
          }
        })
      
      .then(() => {
        let promise = registry[uri];
        if (!promise) {
          throw new Error(`Module ${uri} didn’t register its module`);
        }
        return promise;
      })
    );
  };

  self.define = (depsNames, factory) => {
    const uri = nextDefineUri || ("document" in self ? document.currentScript.src : "") || location.href;
    if (registry[uri]) {
      // Module is already loading or loaded.
      return;
    }
    let exports = {};
    const require = depUri => singleRequire(depUri, uri);
    const specialDeps = {
      module: { uri },
      exports,
      require
    };
    registry[uri] = Promise.all(depsNames.map(
      depName => specialDeps[depName] || require(depName)
    )).then(deps => {
      factory(...deps);
      return exports;
    });
  };
}
define(['./workbox-10cc9e8c'], (function (workbox) { 'use strict';

  self.skipWaiting();
  workbox.clientsClaim();

  /**
   * The precacheAndRoute() method efficiently caches and responds to
   * requests for URLs in the manifest.
   * See https://goo.gl/S9QRab
   */
  workbox.precacheAndRoute([{
    "url": "apple-touch-icon-180x180.png",
    "revision": "03b8e05b6c6279ac3de27c42fe7a2b5d"
  }, {
    "url": "assets/css/index-CFwiKA3C.css",
    "revision": null
  }, {
    "url": "assets/css/vendors/@mdi.css-BJoi0cmu.css",
    "revision": null
  }, {
    "url": "assets/css/vendors/vuetify.css-GyO3t3eb.css",
    "revision": null
  }, {
    "url": "assets/fonts/materialdesignicons-webfont-CSr8KVlo.eot",
    "revision": null
  }, {
    "url": "assets/fonts/materialdesignicons-webfont-Dp5v-WZN.woff2",
    "revision": null
  }, {
    "url": "assets/fonts/materialdesignicons-webfont-PXm3-2wK.woff",
    "revision": null
  }, {
    "url": "assets/img/CubehelixDefault-X1N3hVis.png",
    "revision": null
  }, {
    "url": "assets/img/ebrains-logo-CgeFY5pB.svg",
    "revision": null
  }, {
    "url": "assets/img/eu-logo-BKSH-9fL.png",
    "revision": null
  }, {
    "url": "assets/img/hbp-logo-Y4bOEnBw.png",
    "revision": null
  }, {
    "url": "assets/img/Inferno-BjsXeFlm.png",
    "revision": null
  }, {
    "url": "assets/img/Magma-OFrxUyho.png",
    "revision": null
  }, {
    "url": "assets/img/nest-desktop-logo-light-CCuQsPxC.svg",
    "revision": null
  }, {
    "url": "assets/img/nest-logo-B9eMl2Os.svg",
    "revision": null
  }, {
    "url": "assets/img/norse-logo-CchGHwP5.png",
    "revision": null
  }, {
    "url": "assets/img/Plasma-BQxxwvEK.png",
    "revision": null
  }, {
    "url": "assets/img/Rainbow-B7GZxemw.png",
    "revision": null
  }, {
    "url": "assets/img/Viridis-DnJeo9gN.png",
    "revision": null
  }, {
    "url": "assets/js/index-DyfDGQ9T.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/@codemirror-1TP20Jai.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/@d3-DkeXhe4R.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/@lezer-Bvuw_pfI.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/@marijn-DXwl3gUT.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/@vue-CJ6CJszK.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/axios-Vc0xD52s.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/birpc-l0sNRNKZ.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/codemirror-EcPc0oEr.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/crelt-C8TCjufn.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/deep-pick-omit-CegYQlcN.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/delaunator-DOM67N16.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/destr-CVtkxrq9.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/detect-browser-ClY_l-h2.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/events-CFiqZ6Hr.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/hookable-B8xFkYCm.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/internmap-_doEQLKC.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/js-yaml-Bjkn9eaE.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/moment-G82_0lEo.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/mustache-lDDT9aR0.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/object-hash-CT0JKYsg.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/perfect-debounce-Cp2ysxOb.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/pinia-eyPnjLyI.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/pinia-plugin-persistedstate-BQU3TZ4K.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/plotly-custom.min-db98df80.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/plotly.js-cartesian-dist-min-c5PxYMpO.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/pouchdb-C5xhxh2H.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/robust-predicates-DArCjZZA.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/semver-B1wSxght.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/spark-md5-BcMdwxmq.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/stats.js-DcNFcNYO.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/style-mod-IeDnh0wW.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/three-B5YMmwnN.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/tslog-DHhkq1bn.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/uuid-C6aID195.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vue-codemirror-BT6qtHld.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vue-DftKBQRq.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vue-router-sCSnVpFB.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vuetify-BFSFFw16.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vuetify3-dialog-BebU5cft.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/vuvuzela-C5wpORBy.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/w3c-keyname-Vcq4gwWv.js",
    "revision": null
  }, {
    "url": "assets/js/vendors/webfontloader-Dq_0gWhs.js",
    "revision": null
  }, {
    "url": "favicon.ico",
    "revision": "c7eabf85f6ea5cee9df24c5e334ce3a4"
  }, {
    "url": "logo.svg",
    "revision": "45abf24eec2b3af2056995910d3f2b59"
  }, {
    "url": "maskable-icon-512x512.png",
    "revision": "d6e02b8a94df592fd6e7b61177091c47"
  }, {
    "url": "pwa-192x192.png",
    "revision": "0d75ff859926aebc8e5b8e6fe5132d8c"
  }, {
    "url": "pwa-512x512.png",
    "revision": "0c49fc71b227bca3b535b4397d9ec894"
  }, {
    "url": "pwa-64x64.png",
    "revision": "6e58fba2880ec7c8f7978fb322222aa0"
  }, {
    "url": "registerSW.js",
    "revision": "402b66900e731ca748771b6fc5e7a068"
  }, {
    "url": "apple-touch-icon-180x180.png",
    "revision": "03b8e05b6c6279ac3de27c42fe7a2b5d"
  }, {
    "url": "favicon.ico",
    "revision": "c7eabf85f6ea5cee9df24c5e334ce3a4"
  }, {
    "url": "maskable-icon-512x512.png",
    "revision": "d6e02b8a94df592fd6e7b61177091c47"
  }, {
    "url": "pwa-192x192.png",
    "revision": "0d75ff859926aebc8e5b8e6fe5132d8c"
  }, {
    "url": "pwa-512x512.png",
    "revision": "0c49fc71b227bca3b535b4397d9ec894"
  }, {
    "url": "pwa-64x64.png",
    "revision": "6e58fba2880ec7c8f7978fb322222aa0"
  }, {
    "url": "manifest.webmanifest",
    "revision": "76225708496f88f3518bf3e64ad15db0"
  }], {});
  workbox.cleanupOutdatedCaches();

}));
