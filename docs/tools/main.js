function showOrHide(element, conditionShow, displayShow) {
    element.style.display = conditionShow ? displayShow : 'none';
}

// Comments hiding
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const showComments = urlParams.get('comments') === 'true';
    const allCommentDivs = document.querySelectorAll('div.comment');
    allCommentDivs.forEach(div => {
        showOrHide(div, showComments, 'block');
    });
    const commentsExist = (allCommentDivs.length > 0);
    document.querySelectorAll('a.button-link').forEach(a => {
        if (a.text.includes("Show comments")) {
            showOrHide(a, commentsExist && !showComments, 'inline-block');
        }
        if (a.text.includes("Hide comments")) {
            showOrHide(a, commentsExist && showComments, 'inline-block');
        }
    });
});
