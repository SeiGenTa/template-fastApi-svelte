export const validateEmail = (email: string): string|null => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)){
        return "Invalid email address";
    }
    return null;
}

export const validateUsername = (username: string): string|null => {
    console.log(username);
    if (username.length < 5) {
        return "Username must be at least 5 characters long";
    }
    return null;
}

export const validatePassword = (password: string): string|null => {
    if (password.length < 8) {
        return "Password must be at least 8 characters long";
    }
    if (!/[A-Z]/.test(password)) {
        return "Password must contain at least one uppercase letter";
    }
    if (!/[a-z]/.test(password)) {
        return "Password must contain at least one lowercase letter";
    }
    if (!/[0-9]/.test(password)) {
        return "Password must contain at least one number";
    }
    return "";
}