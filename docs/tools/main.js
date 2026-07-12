function showOrHide(element, conditionShow) {
    let emptyOrZero = conditionShow ? '' : '0';
    element.style.height = emptyOrZero;
    element.style.width = emptyOrZero;
    element.style.margin = emptyOrZero;
    element.style.border = emptyOrZero;
    element.style.padding = emptyOrZero;
    element.style.opacity = emptyOrZero;

    element.style.overflow = conditionShow ? '' : 'hidden';
}

function commentsShowOrHideListener() {
    const anchor = window.location.hash;
    const showComments = anchor === '#comments=true';
    const allCommentDivs = document.querySelectorAll('div.comment');
    allCommentDivs.forEach(div => {
        showOrHide(div, showComments);
    });
    const commentsExist = (allCommentDivs.length > 0);
    document.querySelectorAll('a.button-link').forEach(a => {
        if (a.text.includes("Show comments")) {
            showOrHide(a, commentsExist && !showComments);
        }
        if (a.text.includes("Hide comments")) {
            showOrHide(a, commentsExist && showComments);
        }
    });
}

document.addEventListener('DOMContentLoaded', commentsShowOrHideListener);
window.addEventListener('hashchange', commentsShowOrHideListener);
