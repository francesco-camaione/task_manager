import { useState } from "react"
import { create_user } from "../services/create_user"

const CreateId: React.FC = () => {
    const [JWT, setJWT] = useState<any>(null)

    async function createUser() {
        await create_user()
            .then(async (res) => {
                if (res.ok) {
                    setJWT(await res.json())
                }
            })
            .catch(err =>{
                throw new Error(err)
            })
    }

    return (
        <div>
            <button onClick={() => createUser()}>Create ID</button>
            {JWT?.response}
        </div>
    )
}

export default CreateId