import React from 'react'
import styles from "./bubble.module.css";
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();

  const handlePlayClick = () => {
    navigate("/main");
  };

  return (
    <div>
      <TitleText />
      <button onClick={handlePlayClick}>Log In</button>
      <button onClick={handlePlayClick}>Sign Up</button>
    </div>
  );
}

const TitleText = () => {
  return (
    <>
      <h1 className="text-center text-9xl font-thin text-indigo-300">
        {"Gladiator Go".split("").map((child, idx) => (
          <span className={styles.hoverText} key={idx}>
            {child}
          </span>
        ))}
      </h1>
    </>
  );
};

export default LandingPage