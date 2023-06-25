import { fetcher } from "../utils/utils"

export async function create_user(): Promise<Response> {
    const url = "/create_user"
    return await fetcher(url, "POST", "")
}