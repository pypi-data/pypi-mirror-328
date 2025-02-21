import { i as ge, a as z, r as Ie, w as O, g as ye, b as be } from "./Index-CaCCrlVx.js";
const E = window.ms_globals.React, oe = window.ms_globals.React.useMemo, we = window.ms_globals.React.forwardRef, _e = window.ms_globals.React.useRef, he = window.ms_globals.React.useState, ve = window.ms_globals.React.useEffect, q = window.ms_globals.ReactDOM.createPortal, xe = window.ms_globals.internalContext.useContextPropsContext, Ee = window.ms_globals.internalContext.ContextPropsProvider, Se = window.ms_globals.antd.Upload;
var Re = /\s/;
function Ce(e) {
  for (var t = e.length; t-- && Re.test(e.charAt(t)); )
    ;
  return t;
}
var Pe = /^\s+/;
function Fe(e) {
  return e && e.slice(0, Ce(e) + 1).replace(Pe, "");
}
var K = NaN, Le = /^[-+]0x[0-9a-f]+$/i, ke = /^0b[01]+$/i, Ue = /^0o[0-7]+$/i, Te = parseInt;
function J(e) {
  if (typeof e == "number")
    return e;
  if (ge(e))
    return K;
  if (z(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = z(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Fe(e);
  var r = ke.test(e);
  return r || Ue.test(e) ? Te(e.slice(2), r ? 2 : 8) : Le.test(e) ? K : +e;
}
var A = function() {
  return Ie.Date.now();
}, Oe = "Expected a function", je = Math.max, De = Math.min;
function Ne(e, t, r) {
  var s, i, n, o, c, d, v = 0, g = !1, l = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Oe);
  t = J(t) || 0, z(r) && (g = !!r.leading, l = "maxWait" in r, n = l ? je(J(r.maxWait) || 0, t) : n, w = "trailing" in r ? !!r.trailing : w);
  function f(u) {
    var b = s, F = i;
    return s = i = void 0, v = u, o = e.apply(F, b), o;
  }
  function h(u) {
    return v = u, c = setTimeout(_, t), g ? f(u) : o;
  }
  function C(u) {
    var b = u - d, F = u - v, T = t - b;
    return l ? De(T, n - F) : T;
  }
  function m(u) {
    var b = u - d, F = u - v;
    return d === void 0 || b >= t || b < 0 || l && F >= n;
  }
  function _() {
    var u = A();
    if (m(u))
      return p(u);
    c = setTimeout(_, C(u));
  }
  function p(u) {
    return c = void 0, w && s ? f(u) : (s = i = void 0, o);
  }
  function P() {
    c !== void 0 && clearTimeout(c), v = 0, s = d = i = c = void 0;
  }
  function a() {
    return c === void 0 ? o : p(A());
  }
  function R() {
    var u = A(), b = m(u);
    if (s = arguments, i = this, d = u, b) {
      if (c === void 0)
        return h(d);
      if (l)
        return clearTimeout(c), c = setTimeout(_, t), f(d);
    }
    return c === void 0 && (c = setTimeout(_, t)), o;
  }
  return R.cancel = P, R.flush = a, R;
}
var ie = {
  exports: {}
}, N = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var We = E, Ae = Symbol.for("react.element"), Me = Symbol.for("react.fragment"), qe = Object.prototype.hasOwnProperty, ze = We.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Be = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function se(e, t, r) {
  var s, i = {}, n = null, o = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) qe.call(t, s) && !Be.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Ae,
    type: e,
    key: n,
    ref: o,
    props: i,
    _owner: ze.current
  };
}
N.Fragment = Me;
N.jsx = se;
N.jsxs = se;
ie.exports = N;
var S = ie.exports;
const {
  SvelteComponent: Ge,
  assign: X,
  binding_callbacks: Y,
  check_outros: He,
  children: ce,
  claim_element: le,
  claim_space: Ke,
  component_subscribe: Q,
  compute_slots: Je,
  create_slot: Xe,
  detach: U,
  element: ae,
  empty: Z,
  exclude_internal_props: V,
  get_all_dirty_from_scope: Ye,
  get_slot_changes: Qe,
  group_outros: Ze,
  init: Ve,
  insert_hydration: j,
  safe_not_equal: $e,
  set_custom_element_data: ue,
  space: et,
  transition_in: D,
  transition_out: B,
  update_slot_base: tt
} = window.__gradio__svelte__internal, {
  beforeUpdate: nt,
  getContext: rt,
  onDestroy: ot,
  setContext: it
} = window.__gradio__svelte__internal;
function $(e) {
  let t, r;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Xe(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ae("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = le(n, "SVELTE-SLOT", {
        class: !0
      });
      var o = ce(t);
      i && i.l(o), o.forEach(U), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(n, o) {
      j(n, t, o), i && i.m(t, null), e[9](t), r = !0;
    },
    p(n, o) {
      i && i.p && (!r || o & /*$$scope*/
      64) && tt(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        r ? Qe(
          s,
          /*$$scope*/
          n[6],
          o,
          null
        ) : Ye(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (D(i, n), r = !0);
    },
    o(n) {
      B(i, n), r = !1;
    },
    d(n) {
      n && U(t), i && i.d(n), e[9](null);
    }
  };
}
function st(e) {
  let t, r, s, i, n = (
    /*$$slots*/
    e[4].default && $(e)
  );
  return {
    c() {
      t = ae("react-portal-target"), r = et(), n && n.c(), s = Z(), this.h();
    },
    l(o) {
      t = le(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), ce(t).forEach(U), r = Ke(o), n && n.l(o), s = Z(), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(o, c) {
      j(o, t, c), e[8](t), j(o, r, c), n && n.m(o, c), j(o, s, c), i = !0;
    },
    p(o, [c]) {
      /*$$slots*/
      o[4].default ? n ? (n.p(o, c), c & /*$$slots*/
      16 && D(n, 1)) : (n = $(o), n.c(), D(n, 1), n.m(s.parentNode, s)) : n && (Ze(), B(n, 1, 1, () => {
        n = null;
      }), He());
    },
    i(o) {
      i || (D(n), i = !0);
    },
    o(o) {
      B(n), i = !1;
    },
    d(o) {
      o && (U(t), U(r), U(s)), e[8](null), n && n.d(o);
    }
  };
}
function ee(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function ct(e, t, r) {
  let s, i, {
    $$slots: n = {},
    $$scope: o
  } = t;
  const c = Je(n);
  let {
    svelteInit: d
  } = t;
  const v = O(ee(t)), g = O();
  Q(e, g, (a) => r(0, s = a));
  const l = O();
  Q(e, l, (a) => r(1, i = a));
  const w = [], f = rt("$$ms-gr-react-wrapper"), {
    slotKey: h,
    slotIndex: C,
    subSlotIndex: m
  } = ye() || {}, _ = d({
    parent: f,
    props: v,
    target: g,
    slot: l,
    slotKey: h,
    slotIndex: C,
    subSlotIndex: m,
    onDestroy(a) {
      w.push(a);
    }
  });
  it("$$ms-gr-react-wrapper", _), nt(() => {
    v.set(ee(t));
  }), ot(() => {
    w.forEach((a) => a());
  });
  function p(a) {
    Y[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function P(a) {
    Y[a ? "unshift" : "push"](() => {
      i = a, l.set(i);
    });
  }
  return e.$$set = (a) => {
    r(17, t = X(X({}, t), V(a))), "svelteInit" in a && r(5, d = a.svelteInit), "$$scope" in a && r(6, o = a.$$scope);
  }, t = V(t), [s, i, g, l, c, d, o, n, p, P];
}
class lt extends Ge {
  constructor(t) {
    super(), Ve(this, t, ct, st, $e, {
      svelteInit: 5
    });
  }
}
const {
  SvelteComponent: It
} = window.__gradio__svelte__internal, te = window.ms_globals.rerender, M = window.ms_globals.tree;
function at(e, t = {}) {
  function r(s) {
    const i = O(), n = new lt({
      ...s,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const c = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, d = o.parent ?? M;
          return d.nodes = [...d.nodes, c], te({
            createPortal: q,
            node: M
          }), o.onDestroy(() => {
            d.nodes = d.nodes.filter((v) => v.svelteInstance !== i), te({
              createPortal: q,
              node: M
            });
          }), c;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(r);
    });
  });
}
function ut(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function dt(e, t = !1) {
  try {
    if (be(e))
      return e;
    if (t && !ut(e))
      return;
    if (typeof e == "string") {
      let r = e.trim();
      return r.startsWith(";") && (r = r.slice(1)), r.endsWith(";") && (r = r.slice(0, -1)), new Function(`return (...args) => (${r})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function y(e, t) {
  return oe(() => dt(e, t), [e, t]);
}
const ft = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function mt(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = pt(r, s), t;
  }, {}) : {};
}
function pt(e, t) {
  return typeof t == "number" && !ft.includes(e) ? t + "px" : t;
}
function G(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const i = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: c
        } = G(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: c,
          children: [...E.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(q(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: c,
      useCapture: d
    }) => {
      r.addEventListener(c, o, d);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: c
      } = G(n);
      t.push(...c), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function wt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const ne = we(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: i
}, n) => {
  const o = _e(), [c, d] = he([]), {
    forceClone: v
  } = xe(), g = v ? !0 : t;
  return ve(() => {
    var C;
    if (!o.current || !e)
      return;
    let l = e;
    function w() {
      let m = l;
      if (l.tagName.toLowerCase() === "svelte-slot" && l.children.length === 1 && l.children[0] && (m = l.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), wt(n, m), r && m.classList.add(...r.split(" ")), s) {
        const _ = mt(s);
        Object.keys(_).forEach((p) => {
          m.style[p] = _[p];
        });
      }
    }
    let f = null, h = null;
    if (g && window.MutationObserver) {
      let m = function() {
        var a, R, u;
        (a = o.current) != null && a.contains(l) && ((R = o.current) == null || R.removeChild(l));
        const {
          portals: p,
          clonedElement: P
        } = G(e);
        l = P, d(p), l.style.display = "contents", h && clearTimeout(h), h = setTimeout(() => {
          w();
        }, 50), (u = o.current) == null || u.appendChild(l);
      };
      m();
      const _ = Ne(() => {
        m(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      f = new window.MutationObserver(_), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      l.style.display = "contents", w(), (C = o.current) == null || C.appendChild(l);
    return () => {
      var m, _;
      l.style.display = "", (m = o.current) != null && m.contains(l) && ((_ = o.current) == null || _.removeChild(l)), f == null || f.disconnect();
    };
  }, [e, g, r, s, n, i]), E.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...c);
}), _t = ({
  children: e,
  ...t
}) => /* @__PURE__ */ S.jsx(S.Fragment, {
  children: e(t)
});
function ht(e) {
  return E.createElement(_t, {
    children: e
  });
}
function re(e, t) {
  return e ? t != null && t.forceClone || t != null && t.params ? ht((r) => /* @__PURE__ */ S.jsx(Ee, {
    forceClone: t == null ? void 0 : t.forceClone,
    params: t == null ? void 0 : t.params,
    children: /* @__PURE__ */ S.jsx(ne, {
      slot: e,
      clone: t == null ? void 0 : t.clone,
      ...r
    })
  })) : /* @__PURE__ */ S.jsx(ne, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function k({
  key: e,
  slots: t,
  targets: r
}, s) {
  return t[e] ? (...i) => r ? r.map((n, o) => /* @__PURE__ */ S.jsx(E.Fragment, {
    children: re(n, {
      clone: !0,
      params: i,
      forceClone: !0
    })
  }, o)) : /* @__PURE__ */ S.jsx(S.Fragment, {
    children: re(t[e], {
      clone: !0,
      params: i,
      forceClone: !0
    })
  }) : void 0;
}
function vt(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const yt = at(({
  slots: e,
  upload: t,
  showUploadList: r,
  progress: s,
  beforeUpload: i,
  customRequest: n,
  previewFile: o,
  isImageUrl: c,
  itemRender: d,
  iconRender: v,
  data: g,
  onChange: l,
  onValueChange: w,
  onRemove: f,
  fileList: h,
  setSlotParams: C,
  ...m
}) => {
  const _ = e["showUploadList.downloadIcon"] || e["showUploadList.removeIcon"] || e["showUploadList.previewIcon"] || e["showUploadList.extra"] || typeof r == "object", p = vt(r), P = y(p.showPreviewIcon), a = y(p.showRemoveIcon), R = y(p.showDownloadIcon), u = y(i), b = y(n), F = y(s == null ? void 0 : s.format), T = y(o), de = y(c), fe = y(d), me = y(v), pe = y(g), H = oe(() => (h == null ? void 0 : h.map((I) => ({
    ...I,
    name: I.orig_name || I.path,
    uid: I.url || I.path,
    status: "done"
  }))) || [], [h]);
  return /* @__PURE__ */ S.jsx(Se.Dragger, {
    ...m,
    fileList: H,
    data: pe || g,
    previewFile: T,
    isImageUrl: de,
    itemRender: e.itemRender ? k({
      slots: e,
      key: "itemRender"
    }) : fe,
    iconRender: e.iconRender ? k({
      slots: e,
      key: "iconRender"
    }) : me,
    onRemove: (I) => {
      f == null || f(I);
      const W = H.findIndex((x) => x.uid === I.uid), L = h.slice();
      L.splice(W, 1), w == null || w(L), l == null || l(L.map((x) => x.path));
    },
    beforeUpload: async (I, W) => {
      if (u && !await u(I, W))
        return !1;
      const L = (await t([I])).filter((x) => x);
      return w == null || w([...h, ...L]), l == null || l([...h.map((x) => x.path), ...L.map((x) => x.path)]), !1;
    },
    maxCount: 1,
    customRequest: b,
    progress: s && {
      ...s,
      format: F
    },
    showUploadList: _ ? {
      ...p,
      showDownloadIcon: R || p.showDownloadIcon,
      showRemoveIcon: a || p.showRemoveIcon,
      showPreviewIcon: P || p.showPreviewIcon,
      downloadIcon: e["showUploadList.downloadIcon"] ? k({
        slots: e,
        key: "showUploadList.downloadIcon"
      }) : p.downloadIcon,
      removeIcon: e["showUploadList.removeIcon"] ? k({
        slots: e,
        key: "showUploadList.removeIcon"
      }) : p.removeIcon,
      previewIcon: e["showUploadList.previewIcon"] ? k({
        slots: e,
        key: "showUploadList.previewIcon"
      }) : p.previewIcon,
      extra: e["showUploadList.extra"] ? k({
        slots: e,
        key: "showUploadList.extra"
      }) : p.extra
    } : r
  });
});
export {
  yt as UploadDragger,
  yt as default
};
