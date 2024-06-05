import React, {ButtonHTMLAttributes} from "react";

import { BackgroundColorClasses, TextColorClasses } from "../enums";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    backgroundColor?: string,
    classProps?: string,
    fontColor?: string,
    redirectUrl?: string,
    text: string,
}

export default ({backgroundColor = BackgroundColorClasses.SteelBlueBackground, classProps, fontColor = TextColorClasses.TextWhite, onClick, redirectUrl, text, ...props}: ButtonProps) => {
    const dropShadow = backgroundColor === BackgroundColorClasses.Transparent ? '' : 'drop-shadow-lg'
    const buttonClassName = `px-4 rounded-lg ${backgroundColor} ${fontColor} ${dropShadow} focus:outline-none ${classProps ? classProps : ''}`
    const handleClick: React.MouseEventHandler<HTMLButtonElement> = (event) => {
        if (redirectUrl) {
            window.location.href = redirectUrl;  // Perform the redirection
        } else if (onClick) {
            onClick(event)
        }
    }

    return <button className={buttonClassName} onClick={handleClick} {...props}>{text}</button>
}