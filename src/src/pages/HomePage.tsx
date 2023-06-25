import React from "react"
import CreateId from "../components/CreateId"

const HomePage: React.FC = () => {

    return (
        <>
            <h1>Task manager</h1>
            <p>Manage tasks should not require more than 10m per day.</p>
            <p>The goal of this app is to achieve this goal
                by keep it as minimal as possible</p>
            <CreateId />
        </>
    )
}

export default HomePage