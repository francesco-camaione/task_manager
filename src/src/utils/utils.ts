export function fetcher(url: string, method: string, body?: string): Promise<Response> {
    const req_body = method !== "GET" ? body : null
    const promise = fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: req_body
    })
    return promise

}