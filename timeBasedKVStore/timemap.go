// https://leetcode.com/problems/time-based-key-value-store/description/
package timebasedkvstore

type data struct {
	k int
	v string
}

type TimeMap struct {
	m map[string]*[]data
}

func Constructor() TimeMap {
	return TimeMap{make(map[string]*[]data)}
}

func (t *TimeMap) Set(key string, value string, timestamp int) {
	if vals, ok := t.m[key]; ok {
		*vals = append(*vals, data{timestamp, value})
		return
	}

	t.m[key] = &[]data{{timestamp, value}}
}

func (t *TimeMap) Get(key string, timestamp int) string {
	valp, ok := t.m[key]
	if !ok {
		return ""
	}

	vals := *valp

	var (
		value string
		l, r  = 0, len(vals) - 1
	)
	for l <= r {
		m := l + (r-l)/2
		if vals[m].k <= timestamp {
			value = vals[m].v
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return value
}
