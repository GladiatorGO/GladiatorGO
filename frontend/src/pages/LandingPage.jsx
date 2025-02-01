import React from 'react'
import styles from "./bubble.module.css";

function LandingPage() {
  return (
    <div>
      <TitleText />
    </div>
  )
}

const TitleText = () => {
  return (
    <h1 className="text-center text-9xl font-thin text-indigo-300">
      {"Gladiator Go".split("").map((child, idx) => (
        <span className={styles.hoverText} key={idx}>
          {child}
        </span>
      ))}
    </h1>
  );
};

export default LandingPage