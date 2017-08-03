template="""package zdesk

import (
	"errors"
	"fmt"
	"io/ioutil"
    "net/http"
)

func handle (resp *http.Response, ro *RequestOptions, err error) ([]byte, error) {{
	if err != nil {{
		return nil, err
	}}

	if ro != nil {{
		if ro.ResponseOption == "location" {{
			return []byte(resp.Header.Get("Location")), nil
		}}

		if ro.ResponseOption == "code" {{
			return []byte(fmt.Sprintf("%d", resp.StatusCode)), nil
		}}
	}}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {{
		return nil, err
	}}

	return body, nil
}}

{}
"""
