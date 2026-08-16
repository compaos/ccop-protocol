export declare const GENESIS_HASH: string;
export declare const SAFE_INT_MAX = 9007199254740991;
export declare class CCOPError extends Error {
}
export declare function canonicalTimestamp(s: string): string;
export declare function canonicalJson(v: any): string;
export declare function deepNormalize(v: any): any;
export declare function effectHash(obj: any): any;
export declare function eventHash(obj: any): any;
export declare function moneyAdd(items: any[], currency: string, scale: number): {
    amount: string;
    scale: number;
    currency: string;
};
export declare function fxSettle(original: any, rate: string, rateScale: number, targetCurrency: string, targetScale: number): {
    amount: string;
    scale: number;
    currency: string;
};
export declare function pointerGet(obj: any, path: string): any;
export declare function ccopGlob(pattern: string, value: string): boolean;
export declare function evalOp(left: any, op: string, right?: any): boolean;
export declare function policyDecision(effect: any, rules: any[]): "ALLOW" | "DENY" | "REQUIRE_APPROVAL";
export declare function writerAllowed(reg: any, actor: any, eventType: string): any;
export declare function leaseConsumed(events: any[], ref: any): number;
export declare function approvalLeases(events: any[], ref: any): number;
export declare function counterPrecheck(current: number, maximum: number): boolean;
export declare function controlAssertionTrusted(ref: any, obj: any): boolean;
