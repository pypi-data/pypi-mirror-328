import { i as Se, a as K, r as Le, w as D, g as Fe, b as Ce } from "./Index-BpI8SKDC.js";
const L = window.ms_globals.React, ue = window.ms_globals.React.useMemo, Re = window.ms_globals.React.forwardRef, de = window.ms_globals.React.useRef, fe = window.ms_globals.React.useState, me = window.ms_globals.React.useEffect, H = window.ms_globals.ReactDOM.createPortal, Pe = window.ms_globals.internalContext.useContextPropsContext, Ue = window.ms_globals.internalContext.ContextPropsProvider, ke = window.ms_globals.antd.Upload;
var Te = /\s/;
function Oe(e) {
  for (var t = e.length; t-- && Te.test(e.charAt(t)); )
    ;
  return t;
}
var je = /^\s+/;
function Ne(e) {
  return e && e.slice(0, Oe(e) + 1).replace(je, "");
}
var V = NaN, We = /^[-+]0x[0-9a-f]+$/i, Ae = /^0b[01]+$/i, De = /^0o[0-7]+$/i, Me = parseInt;
function $(e) {
  if (typeof e == "number")
    return e;
  if (Se(e))
    return V;
  if (K(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = K(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ne(e);
  var r = Ae.test(e);
  return r || De.test(e) ? Me(e.slice(2), r ? 2 : 8) : We.test(e) ? V : +e;
}
function ze() {
}
var B = function() {
  return Le.Date.now();
}, qe = "Expected a function", Be = Math.max, Ge = Math.min;
function He(e, t, r) {
  var s, i, n, o, l, d, h = 0, g = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(qe);
  t = $(t) || 0, K(r) && (g = !!r.leading, c = "maxWait" in r, n = c ? Be($(r.maxWait) || 0, t) : n, w = "trailing" in r ? !!r.trailing : w);
  function f(u) {
    var b = s, P = i;
    return s = i = void 0, h = u, o = e.apply(P, b), o;
  }
  function v(u) {
    return h = u, l = setTimeout(_, t), g ? f(u) : o;
  }
  function E(u) {
    var b = u - d, P = u - h, A = t - b;
    return c ? Ge(A, n - P) : A;
  }
  function m(u) {
    var b = u - d, P = u - h;
    return d === void 0 || b >= t || b < 0 || c && P >= n;
  }
  function _() {
    var u = B();
    if (m(u))
      return y(u);
    l = setTimeout(_, E(u));
  }
  function y(u) {
    return l = void 0, w && s ? f(u) : (s = i = void 0, o);
  }
  function p() {
    l !== void 0 && clearTimeout(l), h = 0, s = d = i = l = void 0;
  }
  function a() {
    return l === void 0 ? o : y(B());
  }
  function C() {
    var u = B(), b = m(u);
    if (s = arguments, i = this, d = u, b) {
      if (l === void 0)
        return v(d);
      if (c)
        return clearTimeout(l), l = setTimeout(_, t), f(d);
    }
    return l === void 0 && (l = setTimeout(_, t)), o;
  }
  return C.cancel = p, C.flush = a, C;
}
var pe = {
  exports: {}
}, q = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ke = L, Je = Symbol.for("react.element"), Xe = Symbol.for("react.fragment"), Ye = Object.prototype.hasOwnProperty, Qe = Ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ze = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function we(e, t, r) {
  var s, i = {}, n = null, o = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) Ye.call(t, s) && !Ze.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Je,
    type: e,
    key: n,
    ref: o,
    props: i,
    _owner: Qe.current
  };
}
q.Fragment = Xe;
q.jsx = we;
q.jsxs = we;
pe.exports = q;
var F = pe.exports;
const {
  SvelteComponent: Ve,
  assign: ee,
  binding_callbacks: te,
  check_outros: $e,
  children: _e,
  claim_element: he,
  claim_space: et,
  component_subscribe: ne,
  compute_slots: tt,
  create_slot: nt,
  detach: N,
  element: ge,
  empty: re,
  exclude_internal_props: oe,
  get_all_dirty_from_scope: rt,
  get_slot_changes: ot,
  group_outros: it,
  init: st,
  insert_hydration: M,
  safe_not_equal: lt,
  set_custom_element_data: ve,
  space: ct,
  transition_in: z,
  transition_out: J,
  update_slot_base: at
} = window.__gradio__svelte__internal, {
  beforeUpdate: ut,
  getContext: dt,
  onDestroy: ft,
  setContext: mt
} = window.__gradio__svelte__internal;
function ie(e) {
  let t, r;
  const s = (
    /*#slots*/
    e[7].default
  ), i = nt(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ge("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = he(n, "SVELTE-SLOT", {
        class: !0
      });
      var o = _e(t);
      i && i.l(o), o.forEach(N), this.h();
    },
    h() {
      ve(t, "class", "svelte-1rt0kpf");
    },
    m(n, o) {
      M(n, t, o), i && i.m(t, null), e[9](t), r = !0;
    },
    p(n, o) {
      i && i.p && (!r || o & /*$$scope*/
      64) && at(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        r ? ot(
          s,
          /*$$scope*/
          n[6],
          o,
          null
        ) : rt(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (z(i, n), r = !0);
    },
    o(n) {
      J(i, n), r = !1;
    },
    d(n) {
      n && N(t), i && i.d(n), e[9](null);
    }
  };
}
function pt(e) {
  let t, r, s, i, n = (
    /*$$slots*/
    e[4].default && ie(e)
  );
  return {
    c() {
      t = ge("react-portal-target"), r = ct(), n && n.c(), s = re(), this.h();
    },
    l(o) {
      t = he(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), _e(t).forEach(N), r = et(o), n && n.l(o), s = re(), this.h();
    },
    h() {
      ve(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      M(o, t, l), e[8](t), M(o, r, l), n && n.m(o, l), M(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? n ? (n.p(o, l), l & /*$$slots*/
      16 && z(n, 1)) : (n = ie(o), n.c(), z(n, 1), n.m(s.parentNode, s)) : n && (it(), J(n, 1, 1, () => {
        n = null;
      }), $e());
    },
    i(o) {
      i || (z(n), i = !0);
    },
    o(o) {
      J(n), i = !1;
    },
    d(o) {
      o && (N(t), N(r), N(s)), e[8](null), n && n.d(o);
    }
  };
}
function se(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function wt(e, t, r) {
  let s, i, {
    $$slots: n = {},
    $$scope: o
  } = t;
  const l = tt(n);
  let {
    svelteInit: d
  } = t;
  const h = D(se(t)), g = D();
  ne(e, g, (a) => r(0, s = a));
  const c = D();
  ne(e, c, (a) => r(1, i = a));
  const w = [], f = dt("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: E,
    subSlotIndex: m
  } = Fe() || {}, _ = d({
    parent: f,
    props: h,
    target: g,
    slot: c,
    slotKey: v,
    slotIndex: E,
    subSlotIndex: m,
    onDestroy(a) {
      w.push(a);
    }
  });
  mt("$$ms-gr-react-wrapper", _), ut(() => {
    h.set(se(t));
  }), ft(() => {
    w.forEach((a) => a());
  });
  function y(a) {
    te[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function p(a) {
    te[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    r(17, t = ee(ee({}, t), oe(a))), "svelteInit" in a && r(5, d = a.svelteInit), "$$scope" in a && r(6, o = a.$$scope);
  }, t = oe(t), [s, i, g, c, l, d, o, n, y, p];
}
class _t extends Ve {
  constructor(t) {
    super(), st(this, t, wt, pt, lt, {
      svelteInit: 5
    });
  }
}
const {
  SvelteComponent: Ct
} = window.__gradio__svelte__internal, le = window.ms_globals.rerender, G = window.ms_globals.tree;
function ht(e, t = {}) {
  function r(s) {
    const i = D(), n = new _t({
      ...s,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
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
          }, d = o.parent ?? G;
          return d.nodes = [...d.nodes, l], le({
            createPortal: H,
            node: G
          }), o.onDestroy(() => {
            d.nodes = d.nodes.filter((h) => h.svelteInstance !== i), le({
              createPortal: H,
              node: G
            });
          }), l;
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
function gt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function vt(e, t = !1) {
  try {
    if (Ce(e))
      return e;
    if (t && !gt(e))
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
function x(e, t) {
  return ue(() => vt(e, t), [e, t]);
}
const It = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function yt(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = bt(r, s), t;
  }, {}) : {};
}
function bt(e, t) {
  return typeof t == "number" && !It.includes(e) ? t + "px" : t;
}
function X(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const i = L.Children.toArray(e._reactElement.props.children).map((n) => {
      if (L.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = X(n.props.el);
        return L.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...L.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(H(L.cloneElement(e._reactElement, {
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
      type: l,
      useCapture: d
    }) => {
      r.addEventListener(l, o, d);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = X(n);
      t.push(...l), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function xt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const ce = Re(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: i
}, n) => {
  const o = de(), [l, d] = fe([]), {
    forceClone: h
  } = Pe(), g = h ? !0 : t;
  return me(() => {
    var E;
    if (!o.current || !e)
      return;
    let c = e;
    function w() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), xt(n, m), r && m.classList.add(...r.split(" ")), s) {
        const _ = yt(s);
        Object.keys(_).forEach((y) => {
          m.style[y] = _[y];
        });
      }
    }
    let f = null, v = null;
    if (g && window.MutationObserver) {
      let m = function() {
        var a, C, u;
        (a = o.current) != null && a.contains(c) && ((C = o.current) == null || C.removeChild(c));
        const {
          portals: y,
          clonedElement: p
        } = X(e);
        c = p, d(y), c.style.display = "contents", v && clearTimeout(v), v = setTimeout(() => {
          w();
        }, 50), (u = o.current) == null || u.appendChild(c);
      };
      m();
      const _ = He(() => {
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
      c.style.display = "contents", w(), (E = o.current) == null || E.appendChild(c);
    return () => {
      var m, _;
      c.style.display = "", (m = o.current) != null && m.contains(c) && ((_ = o.current) == null || _.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, g, r, s, n, i]), L.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
}), Et = ({
  children: e,
  ...t
}) => /* @__PURE__ */ F.jsx(F.Fragment, {
  children: e(t)
});
function Rt(e) {
  return L.createElement(Et, {
    children: e
  });
}
function ae(e, t) {
  return e ? t != null && t.forceClone || t != null && t.params ? Rt((r) => /* @__PURE__ */ F.jsx(Ue, {
    forceClone: t == null ? void 0 : t.forceClone,
    params: t == null ? void 0 : t.params,
    children: /* @__PURE__ */ F.jsx(ce, {
      slot: e,
      clone: t == null ? void 0 : t.clone,
      ...r
    })
  })) : /* @__PURE__ */ F.jsx(ce, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function j({
  key: e,
  slots: t,
  targets: r
}, s) {
  return t[e] ? (...i) => r ? r.map((n, o) => /* @__PURE__ */ F.jsx(L.Fragment, {
    children: ae(n, {
      clone: !0,
      params: i,
      forceClone: !0
    })
  }, o)) : /* @__PURE__ */ F.jsx(F.Fragment, {
    children: ae(t[e], {
      clone: !0,
      params: i,
      forceClone: !0
    })
  }) : void 0;
}
const St = (e) => !!e.name;
function Lt(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const Pt = ht(({
  slots: e,
  upload: t,
  showUploadList: r,
  progress: s,
  beforeUpload: i,
  customRequest: n,
  previewFile: o,
  isImageUrl: l,
  itemRender: d,
  iconRender: h,
  data: g,
  onChange: c,
  onValueChange: w,
  onRemove: f,
  maxCount: v,
  fileList: E,
  setSlotParams: m,
  ..._
}) => {
  const y = e["showUploadList.downloadIcon"] || e["showUploadList.removeIcon"] || e["showUploadList.previewIcon"] || e["showUploadList.extra"] || typeof r == "object", p = Lt(r), a = x(p.showPreviewIcon), C = x(p.showRemoveIcon), u = x(p.showDownloadIcon), b = x(i), P = x(n), A = x(s == null ? void 0 : s.format), Ie = x(o), ye = x(l), be = x(d), xe = x(h), Ee = x(g), W = de(!1), [U, Y] = fe(E);
  me(() => {
    Y(E);
  }, [E]);
  const Q = ue(() => (U == null ? void 0 : U.map((I) => St(I) ? I : {
    ...I,
    name: I.orig_name || I.path,
    uid: I.uid || I.url || I.path,
    status: "done"
  })) || [], [U]);
  return /* @__PURE__ */ F.jsx(ke, {
    ..._,
    fileList: Q,
    data: Ee || g,
    previewFile: Ie,
    isImageUrl: ye,
    maxCount: 1,
    itemRender: e.itemRender ? j({
      slots: e,
      key: "itemRender"
    }) : be,
    iconRender: e.iconRender ? j({
      slots: e,
      key: "iconRender"
    }) : xe,
    onRemove: (I) => {
      if (W.current)
        return;
      f == null || f(I);
      const T = Q.findIndex((k) => k.uid === I.uid), S = U.slice();
      S.splice(T, 1), w == null || w(S), c == null || c(S.map((k) => k.path));
    },
    customRequest: P || ze,
    beforeUpload: async (I, T) => {
      if (b && !await b(I, T) || W.current)
        return !1;
      W.current = !0;
      let S = T;
      if (typeof v == "number") {
        const R = v - U.length;
        S = T.slice(0, R < 0 ? 0 : R);
      } else if (v === 1)
        S = T.slice(0, 1);
      else if (S.length === 0)
        return W.current = !1, !1;
      Y((R) => [...v === 1 ? [] : R, ...S.map((O) => ({
        ...O,
        size: O.size,
        uid: O.uid,
        name: O.name,
        status: "uploading"
      }))]);
      const k = (await t(S)).filter((R) => R), Z = v === 1 ? k : [...U.filter((R) => !k.some((O) => O.uid === R.uid)), ...k];
      return W.current = !1, w == null || w(Z), c == null || c(Z.map((R) => R.path)), !1;
    },
    progress: s && {
      ...s,
      format: A
    },
    showUploadList: y ? {
      ...p,
      showDownloadIcon: u || p.showDownloadIcon,
      showRemoveIcon: C || p.showRemoveIcon,
      showPreviewIcon: a || p.showPreviewIcon,
      downloadIcon: e["showUploadList.downloadIcon"] ? j({
        slots: e,
        key: "showUploadList.downloadIcon"
      }) : p.downloadIcon,
      removeIcon: e["showUploadList.removeIcon"] ? j({
        slots: e,
        key: "showUploadList.removeIcon"
      }) : p.removeIcon,
      previewIcon: e["showUploadList.previewIcon"] ? j({
        slots: e,
        key: "showUploadList.previewIcon"
      }) : p.previewIcon,
      extra: e["showUploadList.extra"] ? j({
        slots: e,
        key: "showUploadList.extra"
      }) : p.extra
    } : r
  });
});
export {
  Pt as Upload,
  Pt as default
};
